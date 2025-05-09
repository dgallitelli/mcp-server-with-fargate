from aws_cdk import Stack, App
from constructs import Construct

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecs_patterns


class MCPServerStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC
        self.vpc = ec2.Vpc(self, "mcp-server-vpc", max_azs=3)

        # Create Fargate Cluster
        self.ecs_cluster = ecs.Cluster(
            self,
            "mcp-server-ecs-cluster",
            vpc=self.vpc,
        )

        # Define Docker image for the Service
        image = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=ecs.ContainerImage.from_asset(
                directory="src", asset_name="mcp-server-image"
            )
        )

        # Create Fargate Service and ALB
        self.ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "mcp-server-service",
            cluster=self.ecs_cluster,
            cpu=512,
            memory_limit_mib=1024,
            desired_count=1,
            task_image_options=image,
        )


app = App()
MCPServerStack(app, "MCPServer")
app.synth()