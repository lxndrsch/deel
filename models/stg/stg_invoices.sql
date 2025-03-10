select
      invoice_id, 
      parent_invoice_id, 
      transaction_id, 
      organization_id, 
      type, 
      status, 
      currency, 
      payment_currency, 
      payment_method, 
      amount, 
      payment_amount, 
      fx_rate, 
      fx_rate_payment, 
      created_at
from {{ ref('invoices') }}  