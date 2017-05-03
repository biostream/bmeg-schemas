#!/bin/bash -x

export GOPATH=`pwd`
export PATH=$PATH:$GOPATH/bin

go get github.com/golang/protobuf/protoc-gen-go

cd schema && protoc -I . \
    --go_out=plugins=grpc:../bmeg \
	  *.proto