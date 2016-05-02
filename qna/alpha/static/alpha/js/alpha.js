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
        //var $comment_div = $('#ques-' + $id + '-comments');
        var $div = $('#div-for-ques-' + $id + '-comments');

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

    $(document).on('click', '.ans-comments-show', function(e) {
        e.preventDefault();

        var $this = $(this);
        var $href = $this.attr('href');
        var $id = $this.attr('data-item-id');
        //var $comment_div = $('#ans-' + $id + '-comments');
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
});
