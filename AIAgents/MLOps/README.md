# Local Kubernetes with Minikube

Prerequisites
- minikube installed: https://minikube.sigs.k8s.io/
- kubectl installed and configured: https://kubernetes.io/docs/tasks/tools/

Quickstart

1. Start minikube
- Start minikube (customize CPU/memory/driver as needed):
  ```
  minikube start
  # optional: minikube start --cpus=2 --memory=4096 --driver=hyperkit
  ```
- Verify status:
  ```
  minikube status
  # or
  minikube profile list
  # and
  kubectl cluster-info
  # expected output: "Kubernetes control plane is running at https://127.0.0.1:32776
  # CoreDNS is running at https://127.0.0.1:32776/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy"
  ```

3. Make sure kubectl is using the minikube context
- Check current context:
  ```
  kubectl config current-context
  ```
- If not `minikube`, switch to minikube context:
  ```
  kubectl config use-context minikube
  ```

4. Create a Deployment and Service (quick commands)
- Create a deployment (example using nginx):
  ```
  kubectl create deployment simple-ml-ops-app --image=nginx
  ```
- (Optional) scale replicas:
  ```
  kubectl scale deployment/simple-ml-ops-app --replicas=3
  ```
- Expose the deployment as a Service (LoadBalancer type works with minikube via tunnel or minikube service):
  ```
  kubectl expose deployment simple-ml-ops-app --type=LoadBalancer --port=80 --target-port=80
  ```
- Open the service in your browser:
  ```
  # Opens the service in your web browser
  minikube service simple-ml-ops-app

  # Or get a URL (useful in CI or scripts)
  minikube service simple-ml-ops-app --url
  ```

4. Create a Deployment and Service using YAML (recommended for reproducibility)
see `MLOps/deployment.yaml` and `MLOps/service.yaml` for full content:

- Apply manifests:
  ```
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  ```

5. Verify and debug
- Check pods and their status:
  ```
  kubectl get pods -o wide
  ```
- Check services and endpoints:
  ```
  kubectl get svc
  kubectl describe svc simple-ml-ops-app
  ```
- View logs:
  ```
  kubectl logs -l app=simple-ml-ops-app
  ```
- Port-forward to access app without LoadBalancer:
  ```
  kubectl port-forward svc/simple-ml-ops-app 8080:80
  # Then open http://localhost:8080 in your browser, you should see the nginx welcome page
  ```

6. Notes about LoadBalancer on minikube
- By default, minikube supports minikube service and minikube tunnel for LoadBalancer services:
- If you prefer NodePort instead of LoadBalancer:
  ```
  kubectl expose deployment simple-ml-ops-app --type=NodePort --port=80
  kubectl get svc simple-ml-ops-app
  ```

7. Cleanup
- Delete resources:
  ```
  kubectl delete service simple-ml-ops-app
  kubectl delete deployment simple-ml-ops-app
  # or delete by manifests
  kubectl delete -f deployment.yaml -f service.yaml
  ```
- Stop minikube:
  ```
  minikube stop
  minikube delete
  ```

8. Quick verification checklist
- minikube status shows running
- kubectl get pods -> pods are Running
- kubectl get svc -> service has a ClusterIP or external URL via minikube service/tunnel
```