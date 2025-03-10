SELECT 
    org.organization_id, 
    org.first_payment_date, 
    org.last_payment_date, 
    org.legal_entity_country_code, 
    org.count_total_contracts_active, 
    org.created_date
FROM {{ ref('stg_organizations') }} org
