from pymongo import MongoClient

uri = "mongodb+srv://myhao6824:bAgNgwVvY9LP1lXe@cluster0.wt6tr.mongodb.net/"

def print_database_contents():
    try:
        # Kết nối đến MongoDB
        client = MongoClient(uri)
        print("MongoDB connection successful")
        
        # Lấy danh sách các cơ sở dữ liệu
        db_names = client.list_database_names()
        
        for db_name in db_names:
            print(f"Database: {db_name}")
            db = client[db_name]
            
            # Lấy danh sách các collection trong cơ sở dữ liệu
            collection_names = db.list_collection_names()
            
            for coll_name in collection_names:
                print(f"  Collection: {coll_name}")
                collection = db[coll_name]
                
                # In ra dữ liệu trong từng collection
                documents = collection.find()
                for doc in documents:
                    print(f"    Document: {doc}")
                    
    except Exception as e:
        print("Error connecting to MongoDB:", str(e))

if __name__ == '__main__':
    print_database_contents()
