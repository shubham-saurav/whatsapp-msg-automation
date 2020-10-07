from twilio.rest import Client 
 
account_sid = 'AC50166s05b8c1149b724f46c96b2515f3' 
auth_token = 'ecf04d3988dad375288ae4fb728e4b8a' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good Morning buddy 👍',      
                                to='whatsapp:+919999999999' 
                            ) 
    
    print(message.sid)
