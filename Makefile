
IMAGE_NAME=kopf-memory-exporter
TAG=latest
REGISTRY=localhost:5000

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

tag:
	docker tag $(IMAGE_NAME):$(TAG) $(REGISTRY)/$(IMAGE_NAME):$(TAG)

push: build tag
	docker push $(REGISTRY)/$(IMAGE_NAME):$(TAG)

minikube-load:
	@echo "Loading image into Minikube..."
	minikube image load $(IMAGE_NAME):$(TAG)

minikube-deploy:
	kubectl apply -f manifest/crd.yaml
	kubectl apply -f manifest/obj.yaml
	kubectl apply -f manifest/serviceaccount.yaml
	kubectl apply -f manifest/clusterrole.yaml
	kubectl apply -f manifest/clusterrolebinding.yaml
	kubectl apply -f manifest/service.yaml
	kubectl apply -f manifest/deployment.yaml

minikube-clean:
	kubectl delete -f manifest/deployment.yaml --ignore-not-found
	kubectl delete -f manifest/service.yaml --ignore-not-found
	kubectl delete -f manifest/clusterrolebinding.yaml --ignore-not-found
	kubectl delete -f manifest/clusterrole.yaml --ignore-not-found
	kubectl delete -f manifest/serviceaccount.yaml --ignore-not-found

all: build tag push minikube-load minikube-deploy

clean: minikube-clean