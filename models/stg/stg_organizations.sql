select 
    organization_id,  
    first_payment_date,  
    last_payment_date,  
    legal_entity_country_code,  
    count_total_contracts_active,  
    created_date   
from {{ ref('organizations') }}
--Remove nulls for the sake of simplicity. Discuss later.
where first_payment_date is not null 
    and last_payment_date is not null