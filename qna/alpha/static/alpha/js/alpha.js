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

        console.log(data);

        $.post('/show/ques/' + $ques_id + '/comments/', data);
        $div.html('');
        $.get($href, function(data, status) {
            if (status == 'success') {
                $div_comments.html(data);
                $comment_icon.children().toggleClass('red').toggleClass('gray');
            }
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
        var $div_msg = $('#div-for-ques-' + $ques_id + '-info')
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
});
