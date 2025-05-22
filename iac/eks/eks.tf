module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.1"

  cluster_name                   = var.cluster_name
  cluster_endpoint_public_access = true

  cluster_addons = {
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
  }

  vpc_id                   = module.vpc.vpc_id
  subnet_ids               = module.vpc.public_subnets # Use public subnets for public IPs
  control_plane_subnet_ids = module.vpc.intra_subnets

  # EKS Managed Node Group(s)
  eks_managed_node_group_defaults = {
    ami_type       = "AL2_x86_64"
    instance_types = ["t3.large"]

    attach_cluster_primary_security_group = true
  }

  eks_managed_node_groups = {
    cluster-wg = {
      min_size                    = var.min_size
      max_size                    = var.max_size
      desired_size                = var.desired_size
      instance_types              = var.instance_types
      capacity_type               = var.capacity_type
      associate_public_ip_address = true
      key_name                    = var.key_name


      tags = {
        ExtraTag = "test"
      }
    }
  }

  tags = var.tags
}
