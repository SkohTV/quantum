# Build stage
FROM rust:1.86 AS builder

RUN apt-get update && apt-get install -y protobuf

WORKDIR /quantum

COPY src/ src
COPY Cargo.lock .
COPY Cargo.toml .

RUN cargo build --release 


# Release stage
FROM debian:12-slim AS release

WORKDIR /quantum
COPY --from=builder /quantum/target/release/quantum /quantum/bin

RUN apt-get update && apt-get install -y ca-certificates

ENTRYPOINT ["/quantum/bin"]
