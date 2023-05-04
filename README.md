Flask Application Deployment with Helm Chart
This Helm chart is designed to deploy a Flask application to a Kubernetes cluster. The Flask application serves an API with three endpoints:

/version - returns the version of the application
/is_prime - checks if a number is prime or not
/weather - gets the current weather for a US zip code

Requirements:
Kubernetes cluster
Helm 
Docker
openWeatherAPI
Helm

Installation
Clone the repository:


git clone https://github.com/yourusername/repo-name.git
Change to the repository directory:

cd app-dir-name
Install the Helm chart:


helm install <release-name> .
Replace <release-name> with the desired name of the release.

By default, the chart deploys the Flask application with the following configurations:

Number of replicas: 2
Image repository: yourusername/flask-app
Image tag: latest
Service type: NodePort
Service port: 5000
You can customize the configuration by providing values in a YAML file and using the --values flag when running helm install.

Verify that the application is running:

kubectl get pods
Wait until the status of the pods is Running.

Access the API endpoints:

/version - <cluster-ip>:5000/version
/is_prime - <cluster-ip>:5000/is_prime?num=<number>
/weather - <cluster-ip>:5000/weather?zip=<zip-code>
Replace <cluster-ip> with the IP address of the Kubernetes cluster.

Uninstallation
To uninstall the Helm release, run:


helm uninstall <release-name>
Replace <release-name> with the name of the release. This will delete all resources created by the Helm chart, including the deployment and service.
