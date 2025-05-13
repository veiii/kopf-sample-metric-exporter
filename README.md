# kopf-smaple-metric-exporter

Expose prometheus metrics within kopf operator.

Metrics exposed:
 - run_second_total - Total time object lived.

# Install minikube
```bash
chmod +x ./hack/install-minikube.sh
```

# install and run operator
```bash
pip install -r requirements.txt
kopf run metric_exporter/metric_exporter.py --verbose
```

# add CRD and OBJ
```bash
kubectl apply -f tests/crd.yaml
kubectl apply -f tests/obj.yaml
```

# Metric exposed at http://localhost:9090