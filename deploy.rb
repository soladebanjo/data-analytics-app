package 'docker.io' do
  action :install
end

execute 'start_minikube' do
  command 'minikube start'
  action :run
end

execute 'set_docker_env' do
  command 'eval $(minikube docker-env)'
  action :run
end

execute 'build_docker_image' do
  command 'docker build -t my-python-app:latest .'
  cwd '/path/to/your/application'
  action :run
end

execute 'apply_k8s_deployment' do
  command 'kubectl apply -f /path/to/k8sdeployment.yaml'
  action :run
end

execute 'apply_k8s_service' do
  command 'kubectl apply -f /path/to/k8sservice.yaml'
  action :run
end
