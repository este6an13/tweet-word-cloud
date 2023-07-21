'''
    Course: Computer Programming
    Year: 2019
    
    Student Name: Diego Esteban Quintero Rey
    Username: diquintero

    Program: word_cloud.py
    Project: Tweets Word Cloud 
'''

HTML_page_header = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nube de Palabras</title>
        <script src="http://d3js.org/d3.v3.min.js"></script>
        <script src="d3.layout.cloud.js"></script>
    </head>
    <style>
        body {
            font-family: "Lucida Grande", "Droid Sans", Arial, Helvetica, sans-serif;
        }

        .legend {
            border: 1px solid #555555;
            border-radius: 5px;
            font-size: 0.8em;
            margin: 10px;
            padding: 8px;
        }

        .bld {
            font-weight: bold;
        }
    </style>
    <body>

        <script>
            var frequency_list = [
'''

HTML_page_body = '''
            /* Add your frequency list data here */
            ];

            var color = d3.scale.linear()
                .domain([0, 1, 2, 3, 4, 5, 6, 10, 15, 20, 100])
                .range(["#ddd", "#ccc", "#bbb", "#aaa", "#999", "#888", "#777", "#666", "#555", "#444", "#333", "#222"]);

            d3.layout.cloud()
                .size([850, 300])
                .words(frequency_list)
                .rotate(0)
                .fontSize(function(d) { return d.size; })
                .on("end", draw)
                .start();

            function draw(words) {
                d3.select("body")
                    .append("svg")
                    .attr("width", 900)
                    .attr("height", 350)
                    .attr("class", "wordcloud")
                    .append("g")
                    .attr("transform", "translate(370, 200)")
                    .selectAll("text")
                    .data(words)
                    .enter()
                    .append("text")
                    .style("font-size", function(d) { return d.size + "px"; })
                    .style("fill", function(d, i) { return color(i); })
                    .attr("transform", function(d) {
                        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .text(function(d) { return d.text; });
            }
        </script>

        <div style="width: 40%;">
            <div class="legend">
                Las palabras de uso común son más grandes y ligeramente claras. Las palabras menos comunes son más pequeñas y más oscuras.
            </div>
        </div>

    </body>
    </html>
'''

def read_words(file_name):
    '''
    Read a file with words and frequencies and store the data as a list of pairs:
    [(word1, freq1), (word2, freq2), ...]

    where word is a string and freq is an integer.
    '''
    result = []  # Initialize an empty list to store the pairs.

    with open(file_name, "r") as words_file:
        while True:
            line = words_file.readline()
            if line == "":
                break

            word_and_frequency = line.split()  # Separate each line into word and frequency.
            word_and_frequency[1] = int(word_and_frequency[1])  # Convert the frequency value from str to int.
            result.append(word_and_frequency)  # Add the pair as a sublist to the list to be returned.
    
    # No need to close the file explicitly when using 'with open' context manager.
    # The file will be closed automatically when exiting the 'with' block.

    return result  # Return the list containing pairs of words and their corresponding frequencies.

def get_top_words(words, n=100):
    '''
    Receives a list of words and frequencies and returns the top n
    most frequent words with their respective frequencies.
    call: get_top_words([('w', 1), ('x', 5), ('#y', 8), ('#z', 3), ('@a', 4), ('b', 6)], n=2)
    output: [('b', 6), ('#y', 8)]
    '''
    words_x_freq = [(x[1], x[0]) for x in words]  # Inverts each pair by placing the frequency first and then the word.
    words_x_freq.sort(reverse=True)  # Sorts the generated list in descending order based on frequencies.
    n_most_frequent = words_x_freq[:n]  # Makes a copy of the generated list with only the top n most frequent words.
    result = [(n[1], n[0]) for n in n_most_frequent]  # Inverts the word and frequency again, but this time only for the top n most frequent words.
    return result

def get_top_hashtags(words, n=20):
    '''
    Receives a list of words and frequencies and returns the top n
    most frequent hashtags along with their respective frequencies.
    call: get_top_hashtags([('w', 1), ('x', 5), ('#y', 8), ('#z', 3), ('@a', 4), ('b', 6)], n=2)
    output: [('#y', 8)]
    '''
    hashtags = []
    
    for word_and_frequency in words:
        if word_and_frequency[0][0] == "#":
            hashtags.append(word_and_frequency)  # Adds the pairs whose word starts with '#' to the hashtags list.

    hashtags_x_freq = [(x[1], x[0]) for x in hashtags]  # Inverts the order of each pair to sort the list based on frequency.
    hashtags_x_freq.sort(reverse=True)
    n_most_frequent_hashtags = hashtags_x_freq[:n]  # Creates a copy of the inverted hashtags list, but with only the top n most frequent hashtags.
    result = [(n[1], n[0]) for n in n_most_frequent_hashtags]  # Inverts the list again to deliver the result as requested by the program.
    
    return result

def get_top_users(words, n=20):
    '''
    Receives a list of words and frequencies and returns the top n
    most frequent users along with their respective frequencies.
    call: get_top_users([('w', 1), ('x', 5), ('#y', 8), ('#z', 3), ('@a', 4), ('b', 6)], n=2)
    output: [('@a', 4)]
    '''
    users = []
    for word_and_frequency in words:
        if word_and_frequency[0][0] == "@":
            users.append(word_and_frequency)  # Adds the pairs whose word starts with '@' to the users list.

    users_x_freq = [(x[1], x[0]) for x in users]  # Inverts the order of each pair to sort the list based on frequency.
    users_x_freq.sort(reverse=True)
    n_most_frequent_users = users_x_freq[:n]  # Creates a copy of the inverted users list, but with only the top n most frequent users.
    result = [(n[1], n[0]) for n in n_most_frequent_users]  # Inverts the list again to deliver the result as requested by the program.
    
    return result

def generate_cloud(words, scale, file_name):
    '''
    Generates an HTML page that displays a word cloud from the list of words.
    The output HTML code is written to file_name, which can be opened in a browser.
    The scale parameter controls the size of the words.
    '''
    with open(file_name, 'w') as outfile:
        outfile.write(HTML_page_header)

        for w, f in words:
            outfile.write("{text: '" + w + "', size:" + str(f * scale) + "},")

        outfile.write("{text: 'none', size: 0}\n")  # Adds a final entry for the 'none' word with size 0.
        outfile.write(HTML_page_body)

# The words.txt file must be generated by process_tweets.py
# The resulting HTML files can be opened with a browser

words = read_words('words.txt')
generate_cloud(get_top_words(words, 100), 0.3, 'word_cloud.html')
generate_cloud(get_top_hashtags(words, 20), 5, 'hashtag_cloud.html')
generate_cloud(get_top_users(words, 30), 3, 'user_cloud.html')
