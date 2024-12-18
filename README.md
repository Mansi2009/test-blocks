cd gitea
git clone --recurse-submodules https://github.com/go-gitea/gitea.git

# Create the images for UI, AUTH, VERSION-CRONTROL, WORKFLOW-API-GATEWAY
docker build -f Dockerfile.ui --build-arg REACT_APP_ENV=development -t centurion-centurion-ui:latest .
docker build -f Dockerfile.auth -t centurion-centurion-auth:latest .
cd gitea
docker build -f Dockerfile -t centurion-centurion-version-control:latest .
cd workflow-api-gateway
docker build -f Dockerfile -t centurion-centurion-workflow-api-gateway:latest .

# Start the Minikube 
minikube start

# Start the minikube Tunnel
minikube tunnel

# Start the minikube Dashboard
minikube dashboard

# Install helm chart and install the traefik ingress
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install traefik traefik/traefik --namespace kube-system

# For the ingress services
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/cluster-role.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/clusterrolebinding.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/ingress.yaml

# To load the images to minikube
minikube image load centurion-centurion-ui:latest
minikube image load centurion-centurion-auth:latest
minikube image load centurion-centurion-version-control:latest
minikube image load centurion-centurion-workflow-api-gateway:latest

# To create the postgres-db as service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/centurion-db-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/service.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/init-configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-db/init-db-job.yaml

# To create Keycloak as service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-auth/centurion-auth-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-auth/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-auth/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-auth/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-auth/service.yaml

# To create UI as service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-ui/centurion-ui-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-ui/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-ui/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-ui/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-ui/service.yaml

# To create the version-control as service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/centurion-version-control-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/service.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control/ingress.yaml
--> Register to the http://version-control.centurion.localhost/ with gitea_admin_user username, eDt9HkVDi password and admin@hudsondata.com as email

# To create the runner service for the version-control
1. Go to the Site Administration page in http://version-control.centurion.localhost.
2. Click on Actions, then navigate to Secrets.
3. Create a new runner and copy the Registration Token.
4. Use this token in the centurion-version-control-ci/secret.yaml file as the value for RUNNER_REGISTRATION_TOKEN.
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control-ci/secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control-ci/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control-ci/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control-ci/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-version-control-ci/service.yaml

# To create the workflow-engine(Temporalio server) as a service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine/centurion-workflow-engine-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine/service.yaml

# To create the workflow-engine-api as a service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine-api/secrets.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine-api/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine-api/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine-api/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-engine-api/service.yaml

# To create workflow api gateway as a service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/secrets.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/service.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-workflow-api/ingress.yaml

# to create Grafana as service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-grafana/centurion-grafana-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-grafana/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-grafana/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-grafana/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-grafana/service.yaml

# To create prometheus as a service
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-prometheus/centurion-prometheus-secret.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-prometheus/configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-prometheus/deployment.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-prometheus/pvc.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/centurion-prometheus/service.yaml

# To create the configmaps for the all repositories in the gitea(version-control-engine)
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/system_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_evaluator_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_data_enricher_api_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_data_enricher_db_lookup_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_data_enricher_graph_lookup_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_data_enricher_ml_prediction_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_push_webhook_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_push_db_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_push_queue_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_notification_email_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_notification_slack_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/flows_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_activity_wrapper_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/blocks_transformer_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/flows_wrapper_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/deployments_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/helm_charts_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/helm_chart_flows_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/helm_chart_blocks_init_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/helm_chart_workflow_api_gateway_configmap.yaml
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/source_control_init_files/system_workflow_api_gateway_init_configmap.yaml

# To run the automation script to create the repos and secrets
kubectl apply -f C:/Users/cbollu/Flowx/flowx/k8s/init-version-control-job.yaml


KUBECONFIG_CONTENT:
# Create K8 Service Account
kubectl create serviceaccount ci-cd-user
kubectl create clusterrolebinding ci-cd-user-binding --clusterrole=cluster-admin --serviceaccount=default:ci-cd-user
kubectl get configmap -n kube-system kube-root-ca.crt -o jsonpath="{.data['ca\.crt']}" > ca.crt
USER_TOKEN=$(kubectl create token ci-cd-user --duration=87600h)
# Set the API server endpoint to the in-cluster endpoint
API_SERVER="https://kubernetes.default.svc"
# Set the cluster in the kubeconfig
kubectl config set-cluster in-cluster --server=${API_SERVER} --certificate-authority=ca.crt --embed-certs=true --kubeconfig=ci-cd-kubeconfig
# Set the credentials (Service Account token)
kubectl config set-credentials ci-cd-user --token=${USER_TOKEN} --kubeconfig=ci-cd-kubeconfig
# Set the context
kubectl config set-context ci-cd-user-context --cluster=in-cluster --user=ci-cd-user --namespace=default --kubeconfig=ci-cd-kubeconfig
# Use the context
kubectl config use-context ci-cd-user-context --kubeconfig=ci-cd-kubeconfig

# Create KUBECONFIG_CONTENT as secret
1. copy the code from ci-cd-kubeconfig file after running above steps
2. open this page "http://version-control.centurion.localhost/org/Centurion/settings/actions/secrets" add secret with name KUBECONFIG_CONTENT and value ci-cd-kubeconfig file data


# To enable insecure registry in K8 for helm chart:
## Minikube ssh:
to get the 10.107.176.64 run kubectl get svc | grep centurion-version-control
minikube ssh
echo "10.107.176.64 centurion-version-control.default.svc.cluster.local" | sudo tee -a /etc/hosts
Above should not be a problem in the production, but to validate:
kubectl run -i --tty dnsutils -n development --image=busybox:1.28 --restart=Never -- sh
nslookup centurion-version-control.default.svc.cluster.local

# To access the gitea all apis 
1. Create an access token here "http://version-control.centurion.localhost/user/settings/applications" by providing all the permissions
2. Open keycloak "http://auth.centurion.localhost/" sign in as admin cange the realm configuration to centurion then navigate to Users then Attributes update the value with above created access token for gitea_api_token key

# Bug fix for the sytem/flows_wrapper container
1. For the system/flows _wrpper container update the files in expected_workflows by removing last empty line

# Creating pods for the workers (flows and blocks)
1. Create the blocks for addition, multiple and powers
2. Craete the flow by adding locks as transformers in flows(Noote: while adding flow don't keep any value with Zero just add values to it like max attempt is 1 and timeouts as 10000ms(10s))
3. Create a namespace in workflow
4. deploy flows and blocks as a worker service pods in required namespace(Note: while deploying any block or flow as pod don't use the latest as the tag)


# To start the workflow for flow
1. use this end point "http://wapig.centurion.localhost/docs#/Workflows/start_workflow_api_v1_workflows_start_post"
2. use this request in the body
{
  "workflow_type": "flows_basic_test_e3b13c621f",
  "task_queue": "flows_basic_test_e3b13c621f",
  "namespace": "development",
  "input": {
    "a": 10,
    "b": 40
  },
  "workflow_id": "flows-basic-test-01",
  "execution_timeout_seconds": 3600,
  "run_timeout_seconds": 1800,
  "task_timeout_seconds": 60,
  "workflow_id_reuse_policy": 2,
  "wait_for_completion": true,
  "include_request_data": true,
  "include_block_input_data": false
}
