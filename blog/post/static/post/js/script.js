forbidden_words = {
    'stupid': 'st****',
    'fool': 'f**l',
}

var comments = document.getElementsByClassName('comment_text')
console.log('hi')
console.log(comments.length)

for (let index = 0; index < comments.length; index++) {
    const comment = comments[index]
    const text = comment.textContent;
    console.log(text)
    var words_list = text.split(' ');
    var new_word = ''
    for (let index = 0; index < words_list.length; index++) {
        const element = words_list[index];
        console.log(forbidden_words[element])
        if (index) {
            new_word += ' ';
        }
        if (forbidden_words[element.toLowerCase()] !== undefined) {
            new_word +=  forbidden_words[element.toLowerCase()];
        } else {
            new_word += element;
        }
        
    }
    comment.textContent = new_word;
    
}


var comment_text = document.getElementById('id_comment_text');
comment_text.setAttribute('placeholder', 'write comment')