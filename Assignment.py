import json
with open("insta.txt", encoding='utf-8') as f:
    data = f.read()
#print(data)
chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c)>3]
#print(chunks[0])
def pass_chunks(chunk):
    chunk = chunk.strip()
    sep_chunk = chunk.split('\n')
    user_name = sep_chunk[0]
    no_posts = int(sep_chunk[1].split(" post")[0].replace(",",""))
    no_follower = float(sep_chunk[2].split(" follower")[0].replace(",","").replace("k", "").replace("M", ""))
    if ("k" in sep_chunk[2]):
        no_follower = int(no_follower * 1000)
    elif("M" in sep_chunk[2]):
        no_follower = int(no_follower * 1000000)
    else:
        no_follower = int(no_follower)
    no_following = int(sep_chunk[3].split(" following")[0].replace(",","").replace("k", "").replace("M", ""))
    if ("k" in sep_chunk[3]):
        no_following = int(no_following * 1000)
    elif("M" in sep_chunk[3]):
        no_following = int(no_following * 1000000)
    else:
        no_following = int(no_following)
    name = sep_chunk[4]
    if len(sep_chunk) > 5:        
        type_of_page = sep_chunk[5]
        bio = "\n".join(sep_chunk[6:])
    else:
        type_of_page = "Unknown"
        bio = ""
    #print(user_name,no_posts,no_follower,no_following,name,type_of_page,bio,sep="\n")
    return{"username":user_name,"no_of_post":no_posts,"no_follower":no_follower,"no_following":no_following,"name":name,"type_of_page":type_of_page,"bio":bio}
#print(pass_chunks(chunks[0]))
#           all data of distonary come into list and store in all_chunks list
all_chunks =[]
for chunk in chunks:
    parsed_chunk = pass_chunks(chunk)
    all_chunks.append(parsed_chunk)
#       Print all unsolved data
#print(all_chunks)
#       All data load as a string 
s = json.dumps(all_chunks,indent=4)
print(s)
#       Maximum Posts
max = 0
for chunk in all_chunks:
    if (max<chunk['no_of_post']):
        max = chunk['no_of_post']
        chunk_with_post = chunk
print(chunk_with_post)
#       Maximum Followers
max_foll = 0
for chunk in all_chunks:
    if (max_foll<chunk['no_follower']):
        max_foll = chunk['no_follower']
        chunk_of_follower = chunk
print(chunk_of_follower,sep="\n")
#       Maximum Following
max_following = 0
for chunk in all_chunks:
    if(max_following<chunk['no_following']):
        max_following = chunk['no_following']
        chunk_of_following = chunk
print(chunk_of_following)
#       Types of pages
categories = set()
for chunk in all_chunks:
    categories.add(chunk['type_of_page'])
print(categories,len(categories))