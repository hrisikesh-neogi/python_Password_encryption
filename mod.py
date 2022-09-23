import json
import pymongo
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

client_ = {
        "client_url": "mongodb+srv://shohurekotha:shohurekotha20@cluster0.vxe4d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
        "collection_name": "member_test",
        "database": "SHOHUREKOTHA",
        "path": "H:\\sohure kotha\\database@sk\\dataset\skmembers.csv",
    
        }

class update_data:
    """
    class for updating the id and pr if 
    any data gets deleted from middle, the entire collection will
    be deleted and re-created with the updated data.

    
    """
    def __init__(self, collection_name):
        self.collection_name = collection_name

        client = pymongo.MongoClient(client_['client_url'])
        self.db = client[client_['database']]
        cursor = self.db[self.collection_name].find({})
        self.df = pd.DataFrame(cursor)

    def Repeat(self, x):
        _size = len(x)
        repeated = []
        for i in range(_size):
            k = i + 1
            for j in range(k, _size):
                if x[i] == x[j] and x[i] not in repeated:
                    repeated.append(x[i])
        return repeated
    
    def delete_data(self,name = 'none', wp = 'none', del_collection = 'ex_members'):
#         duplicate_entry = pd.DataFrame()
        """
        to delete the data from the database
        checking the name in if statement and if name is not given then
        it will be checking if any duplicate entry is there in the database
        and if there is any duplicate entry then it will delete the data. 
        param:
            name: (Default is none) { name of the member to be deleted }

        
        """

        for row in self.df.index:
            if name != 'none':
                name = name.strip()
                wp = wp.strip()
                 #if name is given
                if self.df['name'][row]== name and self.df['whatsapp'][row] == wp:
                    data = self.df.iloc[[row]]
                    self.db[del_collection].insert_many(json.loads(data.to_json(orient='records')))
                    self.df = self.df.drop(index=row)
                    return self.df
            else:                                             #if name is not given
                name_data = self.df['name'][row]
                # up_name = name.upper()
               
                name_data_total = self.df[self.df['name'] == name_data]
                

                if len(name_data_total) > 1:
                    # print([name for name in name_data_total['name'] ])
                    # print(name_data_total['email'])
                    mail_list = name_data_total['email'].tolist()
                    mails = self.Repeat(mail_list)

                    # print(mails)
                    for mail in mails:
                        mail_data = name_data_total[name_data_total['email'] == mail]
                        # print(mail_data.index[0])
                        self.df.drop(index=mail_data.index[0], inplace=True)
                    
                else:
                    pass

        return self.df
                


    def id_check(self):

        
        self.df = self.delete_data()
        self.df = self.df.reset_index(drop=True)
        for row in self.df.index:
            id_ = self.df['_id'][row]
            if  id_ == row+1:
                pass
            else:
                id_ = row+1
                self.df['_id'][row] = id_
        return self.df


#update
    def update(self):
            available_pr = self.db['sk_pr'].find({})
            pr = pd.DataFrame(available_pr)
            pr_names = [name for name in pr['Name']]
            
            data = self.id_check()
            for row in data.index:
                if row != 0:
                    pr_name = data['Pr'][row-1]
                    if pr_name in pr_names:
                        if pr_names.index(pr_name) != (len(pr_names)-1):
                            pr_assign = pr_names[pr_names.index(pr_name)+1]
                            data['Pr'][row] = pr_assign
                        else:
                            pr_assign = pr_names[0]
                        
                            data['Pr'][row] = pr_assign
                            # print(pr_names )
                            # print(pr_assign)
                else:
                    pr_assign = pr_names[0]
                    data['Pr'][row] = pr_assign
                
                        
            
            self.db[self.collection_name].drop()
            collection = self.db[self.collection_name]
            data_json = json.loads(data.to_json(orient='records'))
            collection.insert_many(data_json)

    