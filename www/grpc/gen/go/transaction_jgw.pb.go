// Code generated by protoc-gen-jrpc-gateway. DO NOT EDIT.
// source: transaction.proto

/*
Package pactus is a reverse proxy.

It translates gRPC into JSON-RPC 2.0
*/
package pactus

import (
	"context"
	"encoding/json"

	"google.golang.org/protobuf/encoding/protojson"
)

type TransactionJsonRpcService struct {
	client TransactionClient
}

func NewTransactionJsonRpcService(client TransactionClient) TransactionJsonRpcService {
	return TransactionJsonRpcService{
		client: client,
	}
}

func (s *TransactionJsonRpcService) Methods() map[string]func(ctx context.Context, message json.RawMessage) (any, error) {
	return map[string]func(ctx context.Context, params json.RawMessage) (any, error){

		"pactus.transaction.get_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(GetTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.GetTransaction(ctx, req)
		},

		"pactus.transaction.calculate_fee": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(CalculateFeeRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.CalculateFee(ctx, req)
		},

		"pactus.transaction.broadcast_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(BroadcastTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.BroadcastTransaction(ctx, req)
		},

		"pactus.transaction.get_raw_transfer_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(GetRawTransferTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.GetRawTransferTransaction(ctx, req)
		},

		"pactus.transaction.get_raw_bond_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(GetRawBondTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.GetRawBondTransaction(ctx, req)
		},

		"pactus.transaction.get_raw_unbond_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(GetRawUnbondTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.GetRawUnbondTransaction(ctx, req)
		},

		"pactus.transaction.get_raw_withdraw_transaction": func(ctx context.Context, data json.RawMessage) (any, error) {
			req := new(GetRawWithdrawTransactionRequest)
			err := protojson.Unmarshal(data, req)
			if err != nil {
				return nil, err
			}
			return s.client.GetRawWithdrawTransaction(ctx, req)
		},
	}
}
