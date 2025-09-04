



# Qeustion 20 Create a project
# Project Name: FinanceTracker
# Tech Stack:

# Backend: Django + Django REST Framework (DRF)

# Database: PostgreSQL

# Authentication: JWT (with email verification, password reset)

# Deployment: Docker, Docker Compose, DockerHub

# Version Control: Git

# 🔹 Functional Requirements

# Transactions Management:

# Users can create, read, update, delete transactions.

# Transaction fields:

# Amount

# Type: Income / Expense

# Date

# Category (optional)

# Description (optional)

# Filtering:

# By date range

# By transaction type (Income/Expense)

# Search:

# By description or category

# Authentication & Authorization:

# JWT authentication for API endpoints

# Email verification after registration

# Password reset functionality

# API Endpoints Examples:

# POST /api/register/ → User registration

# POST /api/token/ → Login and get JWT

# POST /api/token/refresh/ → Refresh token

# GET /api/transactions/ → List transactions with filter & search

# POST /api/transactions/ → Create transaction

# PUT /api/transactions/<id>/ → Update transaction


# DELETE /api/transactions/<id>/ → Delete transaction

# 🔹 Non-functional Requirements

# Database: PostgreSQL

# Version Control: Git (commits for each major functionality)

# Deployment:

# Dockerfile for backend

# docker-compose.yml with backend + PostgreSQL service

# Push backend image to DockerHub

# Environment variables for secrets (SECRET_KEY, DB_PASSWORD)

# 🔹 Optional Enhancements (Bonus)

# Pagination for transaction list

# Filtering by category

# Aggregate reports: total income, total expense, balance


# Swagger or Redoc API documentation

# Write in answer github link