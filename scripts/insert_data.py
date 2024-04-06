from pymongo import MongoClient
import json

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://dbUserKavisha:dbUserPassword@cluster0.hnkbluq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']

# Define the schemas
error_schema = {
    "ErrorID": {"type": "int", "auto_increment": True, "primary_key": True},
    "Status": {"type": "string"},
    "AckID": {"type": "int"},
    "RejectID": {"type": "int", "foreign_key": "Reject.RejectID"},
    "HeaderID": {"type": "int", "foreign_key": "Header.HeaderID"}
}

reject_schema = {
    "RejectID": {"type": "int", "auto_increment": True, "primary_key": True},
    "TrackingID": {"type": "int"},
    "Status": {"type": "string"},
    "ErrorType": {"type": "int", "foreign_key": "ErrorType.ErrorTypeID"},
    "Product": {"type": "string"},
    "Bureau": {"type": "string"}
}

error_type_schema = {
    "ErrorTypeID": {"type": "int", "auto_increment": True, "primary_key": True},
    "Code": {"type": "string"},
    "Description": {"type": "string"}
}

# Insert the data into MongoDB
def insert_data(collection_name, data):
    collection = db[collection_name]
    inserted_document = collection.insert_one(data)
    print(f"Inserted Document ID: {inserted_document.inserted_id}")

# Define the JSON document
json_data = '''
{
  "STATUS": "COMPLETED",
  "ACKNOWLEDGEMENT-ID": 12345,
  "REJECT": [
    {
      "TRACKING-ID": 12345,
      "STATUS": "ERROR",
      "ERRORS": [
        {
          "CODE": "NA",
          "DESCRIPTION": "ERRR05042024140735UR03U01012500QOS0000080YI52AE 1020PAA010111D N0 1 10621011PAA010602281015PAA010706515775ES0700001290102"
        }
      ],
      "PRODUCT": "CIR",
      "BUREAU": "CIBIL"
    }
  ],
  "HEADER": {
    "CUST-ID": "003OS000007wZO8YAM",
    "APPLICATION-ID": "00QOS0000080Yi52AE",
    "RESPONSE-TYPE": "RESPONSE",
    "REQUEST-RECEIVED-TIME": "2024-04-05 08:37:35"
  }
}
'''

document = json.loads(json_data)

# Insert data into separate tables
error_data = {
    "Status": document["STATUS"],
    "AckID": document["ACKNOWLEDGEMENT-ID"]
}
insert_data("Error", error_data)

header_data = {
    "CustID": document["HEADER"]["CUST-ID"],
    "ApplicationID": document["HEADER"]["APPLICATION-ID"],
    "ResponseType": document["HEADER"]["RESPONSE-TYPE"],
    "RequestReceivedTime": document["HEADER"]["REQUEST-RECEIVED-TIME"]
}
insert_data("Header", header_data)

reject = document["REJECT"][0]
reject_data = {
    "TrackingID": reject["TRACKING-ID"],
    "Status": reject["STATUS"],
    "Product": reject["PRODUCT"],
    "Bureau": reject["BUREAU"]
}
insert_data("Reject", reject_data)

error_type_data = {
    "Code": reject["ERRORS"][0]["CODE"],
    "Description": reject["ERRORS"][0]["DESCRIPTION"]
}
insert_data("ErrorType", error_type_data)

# Close the connection
client.close()
