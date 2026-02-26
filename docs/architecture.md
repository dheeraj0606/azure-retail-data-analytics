Retail Analytics Platform – Azure Architecture
Components

Azure SQL Database (OLTP simulation)

Azure Synapse Workspace (Spark + Pipelines)

Azure Data Lake / OneLake (Delta storage)

Azure Key Vault (Secrets management)

Azure DevOps (CI/CD)

Microsoft Fabric (Semantic model + Power BI)

GitHub (Source control)

Data Flow

Retail data generated in Azure SQL

Synapse Pipeline extracts data

Spark transforms data (Bronze → Silver → Gold)

Gold data stored in Delta format

Fabric semantic model built on Gold

Power BI report created

CI/CD via Azure DevOps YAML pipelines
