#!/bin/bash

sudo snap install microk8s --classic

snap alias microk8s.kubectl kubectl

microk8s.kubectl config view --raw > $HOME/.kube/config

sudo chown -f -R $USER ~/.kube