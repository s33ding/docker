source .env

eksctl get nodegroup --cluster "$CLUSTER_NAME"  --region "$REGION"
