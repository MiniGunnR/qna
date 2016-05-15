$(function() {

    $(document).on('click', '.heart', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');

        $.get($href, function(data, status) {
            if (status === 'success') {
                if ($this.children().hasClass('red')) {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                } else {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                }
            }
        });
    });

    $(document).on('click', '.flag', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');

        $.get($href, function(data, status) {
            if (status === 'success') {
                if ($this.children().hasClass('red')) {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                } else {
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                }
            }
        });
    });

    $(document).on('click', '.ques-comments-show', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $div = $('#div-for-ques-' + $id + '-comments');
        var $div_answer_create = $('#div-for-ques-' + $id + '-answer-create');
        var $div_comment_create = $('#div-for-ques-' + $id + '-comment-create');
        var $comment_icon = $('#ques-' + $id + '-comment-form');
        var $answer_icon = $('#ques-' + $id + '-answer-form');

        if ($div.html() == '' && $this.text() != '0 comments') { // if the following div is empty and comments are not 0
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div.html(data);
                    $div_comment_create.html('');
                    $div_answer_create.html('');
                    if ($comment_icon.children().hasClass('red')) {
                        $comment_icon.children().toggleClass('red').toggleClass('gray');
                    }
                    if ($answer_icon.children().hasClass('red')) {
                        $answer_icon.children().toggleClass('red').toggleClass('gray');
                    }
                }
            });
        } else {
            $div.html('');
        }
    });

    $(document).on('click', '.ans-comments-show', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $div = $('#div-for-ans-' + $id + '-comments');

        if ($div.html() == '' && $this.text() != '0 comments') { // if the following div is empty and comments are not 0
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div.html(data);
                }
            });
        } else {
            $div.html('');
        }
    });

    $(document).on('click', '.comment-form', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $div = $('#div-for-ques-' + $id + '-comment-create');
        var $div_comments = $('#div-for-ques-' + $id + '-comments');
        var $div_answer_create = $('#div-for-ques-' + $id + '-answer-create');
        var $answer_icon = $('#ques-' + $id + '-answer-form');

        if ($div.html() == '') {
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div.html(data);
                    $div_comments.html('');
                    $div_answer_create.html('');
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                    if ($answer_icon.children().hasClass('red')) {
                        $answer_icon.children().toggleClass('red').toggleClass('gray');
                    }
                }
            });
        } else {
            $div.html('');
            $this.children().toggleClass('red');
            $this.children().toggleClass('gray');
        }
    });

    $(document).on('click', '.comment-form-ans-icon', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $div = $('#div-for-ans-' + $id + '-comment-create');
        var $div_comments = $('#div-for-ans-' + $id + '-comments');
        var $div_answer_create = $('#div-for-ans-' + $id + '-answer-create');
        var $answer_icon = $('#ans-' + $id + '-answer-form');

        if ($div.html() == '') {
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div.html(data);
                    $div_comments.html('');
                    $div_answer_create.html('');
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                    if ($answer_icon.children().hasClass('red')) {
                        $answer_icon.children().toggleClass('red').toggleClass('gray');
                    }
                }
            });
        } else {
            $div.html('');
            $this.children().toggleClass('red');
            $this.children().toggleClass('gray');
        }
    });

    $(document).on('submit', '.ques-comment-form', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $ques_id = $this.attr("data-ques-id");
        var data = {
            parent: $ques_id,
            author: $('#ques-' + $ques_id + '-author').val(),
            body: $('#ques-' + $ques_id + '-comment-box').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
        var $href = '/html/ques/' + $ques_id + '/comments/';
        var $div = $('#div-for-ques-' + $ques_id + '-comment-create');
        var $div_comments = $('#div-for-ques-' + $ques_id + '-comments');
        var $comment_icon = $('#ques-' + $ques_id + '-comment-form');
        var $comment_count = $('#ques-' + $ques_id + '-comment-count');
        var $comment_count_num = parseInt($comment_count.text(), 10);

        console.log(data);

        $.post('/show/ques/' + $ques_id + '/comments/', data)
        .done(function(response) {
            $div.html('');
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div_comments.html(data);
                    $comment_icon.children().toggleClass('red').toggleClass('gray');
                    var $new_count = $comment_count_num + 1;
                    $comment_count.text($new_count);
                }
            });
        });
    });

    $(document).on('submit', '.ans-comment-form', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $ans_id = $this.attr("data-ans-id");
        var data = {
            parent: $ans_id,
            author: $('#ans-' + $ans_id + '-author').val(),
            body: $('#ans-' + $ans_id + '-comment-box').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
        var $href = '/html/ans/' + $ans_id + '/comments/';
        var $div = $('#div-for-ans-' + $ans_id + '-comment-create');
        var $div_comments = $('#div-for-ans-' + $ans_id + '-comments');
        var $comment_icon = $('#ans-' + $ans_id + '-comment-form');
        var $comment_count = $('#ans-' + $ans_id + '-comment-count');
        var $comment_count_num = parseInt($comment_count.text(), 10);

        console.log(data);

        $.post('/show/ans/' + $ans_id + '/comments/', data)
        .done(function(response) {
            $div.html('');
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div_comments.html(data);
                    $comment_icon.children().toggleClass('red').toggleClass('gray');
                    var $new_count = $comment_count_num + 1;
                    $comment_count.text($new_count);
                }
            });
        });
    });

    $(document).on('click', '.answer-form', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        var $div = $('#div-for-ques-' + $id + '-answer-create');
        var $div_comment_create = $('#div-for-ques-' + $id + '-comment-create');
        var $div_comments = $('#div-for-ques-' + $id + '-comments');
        var $comment_icon = $('#ques-' + $id + '-comment-form');

        if ($div.html() == '') {
            $.get($href, function(data, status) {
                if (status == 'success') {
                    $div.html(data);
                    $div_comments.html('');
                    $div_comment_create.html('');
                    $this.children().toggleClass('red');
                    $this.children().toggleClass('gray');
                    if ($comment_icon.children().hasClass('red')) {
                        $comment_icon.children().toggleClass('red').toggleClass('gray');
                    }
                }
            });
        } else {
            $div.html('');
            $this.children().toggleClass('red');
            $this.children().toggleClass('gray');
            if ($comment_icon.children().hasClass('red')) {
                $comment_icon.children().toggleClass('red').toggleClass('gray');
            }
        }
    });

    $(document).on('submit', '.ques-answer-form', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $ques_id = $this.attr("data-ques-id");
        var data = {
            parent: $ques_id,
            author: $('#ques-' + $ques_id + '-ans-author').val(),
            body: $('#ques-' + $ques_id + '-answer-box').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
        var $href = '/html/ques/' + $ques_id + '/answer/';
        var $div = $('#div-for-ques-' + $ques_id + '-answer-create');
        var $div_msg = $('#div-for-ques-' + $ques_id + '-info');
        var $answer_icon = $('#ques-' + $ques_id + '-answer-form');

        console.log(data);

        $.post('/api/ques/' + $ques_id + '/answer/', data);
        $div.html('');
        $div_msg.html('Your <b><a href="/question/' + $ques_id + '/" target="_blank">answer</a></b> was posted.');
        $div_msg.addClass('alert alert-info');
        $div_msg.css({
            "margin": "10px",
            "padding": "10px"
        });

        $.get($href, function(data, status) {
            if (status == 'success') {
                $answer_icon.children().toggleClass('red').toggleClass('gray');
            }
        });
    });

    $(document).on('submit', '.ques-answer-form-in-detail-page', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $ques_id = $this.attr("data-ques-id");
        var data = {
            parent: $ques_id,
            author: $('#ques-' + $ques_id + '-ans-author').val(),
            body: $('#ques-' + $ques_id + '-answer-box').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
        var $href = '/html/ques/' + $ques_id + '/answer/';
        var $div = $('#div-for-ques-' + $ques_id + '-answer-create');
        var $div_stream = $('#stream');
        var $answer_icon = $('#ques-' + $ques_id + '-answer-form');

        console.log(data);

        $.post('/api/ques/' + $ques_id + '/answer/', data)
        .done(function( response ) {
                var body = data.body.replace("\n", "<br/>");
                console.log(body);
            $div_stream.prepend('<li>\
                <a href="#">You</a>&nbsp;\
                <small class="gray">Just Now</small> <br/>\
                ' + body + '\
                <hr style="margin-bottom: 10px;"/>\
                <div>\
                    <ul class="stream-view-option">\
                        <li><a href="/html/answer/' + response.id + '/comments/" class="ans-comments-show" data-item-id="' + response.id + '">0 comments</a></li>\
                    </ul>\
                </div>\
                <div>\
                    <ul class="text-right stream-post-option">\
                        <li><a href="/heart/answer/' + response.id + '/" class="heart"><i class="fa fa-heart-o gray"></i></a> &nbsp;</li>\
                        <li><a href="/html/ans/' + response.id + '/comment/form/" id="ans-' + response.id + '-comment-form" class="comment-form-ans-icon" data-item-id="' + response.id + '"><i class="fa fa-comment-o gray"></i></a> &nbsp;</li>\
                    </ul>\
                </div>\
            </li>\
            <div id="div-for-ans-' + response.id + '-comments"></div>\
            <div id="div-for-ans-' + response.id + '-comment-create"></div>');
            $div.html('');
        });

        $.get($href, function(data, status) {
            if (status == 'success') {
                $answer_icon.children().toggleClass('red').toggleClass('gray');
            }
        });
    });
});
