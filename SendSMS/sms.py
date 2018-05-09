import plivo

auth_id = "MAZDVINGE4NWE5MGI2MM"
auth_token = "ZjNjOWRhOWJhYmQ4ZDQ0MGM1YTdlZDMwMTBkNjRm"

client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
message_created = client.messages.create(
    src='919740288161',
    dst='919740288160',
    text='Hello, world!'
)