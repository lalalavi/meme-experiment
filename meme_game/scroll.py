import requests
import json

response = requests.get('https://meme-api.herokuapp.com/gimme/10')
#print(response) # gives you the status code (200 means ok)
#print(response.json()) # gives you all the data with all items
#print(response.json()['postLink']) # allows you to explore one of the items more fully

# for meme in response.json()['memes']:
#     print(meme['title'])
#     print(meme['url'])
#     print() #gives me a space
# # this takes the 10 memes and give me the titles of each and their url :D

for meme in response.json()['memes']:
    if meme['ups'] >= 1000:
        print(meme['title'])
        print(meme['url'])
    else:
        print("skip that one cause it sucked")
    print()
# this only does that if the meme has more than 1000 upvotes




# r = requests.get('https://meme-api-python.herokuapp.com/gimme')
# if r.status_code == 200:
#     data = r.json()
#     memes = data['data']['children']
#     random_meme = random.choice(memes)
#     meme_data = random_meme['data']
#     title = meme_data['title']
#     image = meme_data['url']



# OnScroll event (Taken from Florin Pop's Infinite Scroll - https://codepen.io/FlorinPop17/pen/RwwvKYJ)
# possible like button
#     https://codepen.io/emilandersson/pen/rWwvwq 
#     https://codepen.io/LMarran/pen/zxBELo
#     they should not have scss
#     https://codepen.io/kieranfivestars/pen/PwzjgN this one is pretty and simple
#     https://usejquery.com/css/css-like-buttons/ a bunch of them
#     https://codepen.io/abaicus/pen/gNXdQP/ facebook style
#     https://codepen.io/drumsensei/pen/VjemKy?css-preprocessor=sass this one has a reset condition 
#     https://codepen.io/mateusz800/pen/OJPZXMa pretty and simple too
#     https://codepen.io/Barrydreamt/pen/vopyPz epic 



# # OnScroll event (Taken from Florin Pop's Infinite Scroll - https://codepen.io/FlorinPop17/pen/RwwvKYJ)

# # <div id="id01"></div>

# # <script>
# # var xmlhttp = new XMLHttpRequest();
# # var url = "myTutorials.txt";

# # xmlhttp.onreadystatechange = function() {
# #     if (this.readyState == 4 && this.status == 200) {
# #         var myArr = JSON.parse(this.responseText);
# #         myFunction(myArr);
# #     }
# # };
# # xmlhttp.open("GET", url, true);
# # xmlhttp.send();

# # function myFunction(arr) {
# #     var out = "";
# #     var i;
# #     for(i = 0; i < arr.length; i++) {
# #         out += '<a href="' + arr[i].url + '">' +
# #         arr[i].display + '</a><br>';
# #     }
# #     document.getElementById("id01").innerHTML = out;
# # }
# # </script>


# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# meme_subreddits = ['memes', 'dankmemes', 'meirl']

# @app.route('/')
# def index():
#     return render_template('Feed.html')


# @app.route('/gimme')
# @cross_origin()
# def one_post():
#     sub = random.choice(meme_subreddits)
#     try:
#         re = get_posts(sub, 100)

#     except ResponseException:
#         return jsonify({
#             'status_code': 500,
#             'message': 'Internal Server Error'
#         })

#     r = random.choice(re)

#     while not is_img_link(r["url"]):
#         r = random.choice(re)

#     return jsonify({
#         'title': r["title"],
#         'url': r["url"],
#         'postLink': r["link"],
#         'subreddit': sub
#     })


# @app.route('/gimme/<int:count>')
# @cross_origin()
# def multiple_posts(count):

#     if count > 100:
#         return jsonify({
#             'status_code': 400,
#             'message': 'Please ensure the count is less than 100'
#         })

#     sub = random.choice(meme_subreddits)

#     try:
#         re = get_posts(sub, 100)

#     except ResponseException:
#         return jsonify({
#             'status_code': 500,
#             'message': 'Internal Server Error'
#         })

#     random.shuffle(re)

#     memes = []

#     for post in re:
#         if len(memes) == count:
#             break

#         if is_img_link(post['url']):
#             temp = {
#                 'title': post["title"],
#                 'url': post["url"],
#                 'postLink': post["link"],
#                 'subreddit': sub
#             }

#             memes.append(temp)

#     return jsonify({
#         'memes': memes,
#         'count': len(memes)
#     })


# @app.route('/gimme/<subreddit>')
# @cross_origin()
# def one_post_from_sub(subreddit):
#     try:
#         re = get_posts(subreddit, 100)

#     except Redirect:
#         return jsonify({
#             'status_code': 404,
#             'message': 'Invalid Subreddit'
#         })

#     except ResponseException:
#         return jsonify({
#             'status_code': 500,
#             'message': 'Internal Server Error'
#         })

#     r = random.choice(re)

#     while not is_img_link(r["url"]):
#         r = random.choice(re)

#     return jsonify({
#         'title': r["title"],
#         'url': r["url"],
#         'postLink': r["link"],
#         'subreddit': subreddit
#     })


# @app.route('/gimme/<subreddit>/<int:count>')
# @cross_origin()
# def multiple_posts_from_sub(subreddit, count):

#     if count > 100:
#         return jsonify({
#             'status_code': 400,
#             'message': 'Please ensure the count is less than 100'
#         })

#     try:
#         re = get_posts(subreddit, 100)

#     except Redirect:
#         return jsonify({
#             'status_code': 404,
#             'message': 'Invalid Subreddit'
#         })

#     except ResponseException:
#         return jsonify({
#             'status_code': 500,
#             'message': 'Internal Server Error'
#         })

#     random.shuffle(re)

#     memes = []

#     for post in re:
#         if len(memes) == count:
#             break

#         if is_img_link(post['url']):
#             temp = {
#                 'title': post["title"],
#                 'url': post["url"],
#                 'postLink': post["link"]
#             }

#             memes.append(temp)

#     return jsonify({
#         'memes': memes,
#         'count': len(memes),
#         'subreddit': subreddit
#     })


# @app.route('/sample')
# def sample():
#     re = get_posts(random.choice(meme_subreddits), 100)

#     r = random.choice(re)

#     while not is_img_link(r["url"]):
#         r = random.choice(re)

#     return render_template('sample.html', title=r["title"], img_url=r["url"], shortlink=r["link"])


# @app.route('/test')
# def test():
#     re = get_posts(random.choice(meme_subreddits), 100)

#     return render_template('test.html', re=re)


# @app.errorhandler(404)
# @app.route('/<something>')
# def not_found(something):
#     return render_template('not_found.html')