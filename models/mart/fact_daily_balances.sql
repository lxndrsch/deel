SELECT 
    date_trunc( 'day', created_at) AS transaction_date_day,
    org.organization_id,
    coalesce(sum(inv.amount), 0) AS total_amount,
    coalesce(sum(inv.payment_amount), 0) AS total_payment_amount,
    count(inv.invoice_id) AS total_invoices
FROM {{ ref('stg_invoices') }} inv
JOIN {{ ref('stg_organizations') }} org
    ON inv.organization_id = org.organization_id
{{ dbt_utils.group_by(2) }}