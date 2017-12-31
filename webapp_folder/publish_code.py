
# -*- coding: latin-1 -*-


publish_page = '''<style>

.right_aside_button_wrap { display: none; }
.page_html_wrap { }
    
    .edit_info_form_wrap { margin: 0 auto; position: fixed; bottom: 50px; top: 75px; right: 50px; left: 200px; }
    .edit_info_form_data { width: 100%; border: 20px solid #002b36; height: 100%; position: relative; background-color: #073642; }
    
    form { border-left: 1px solid #657b83; border-right: 1px solid #657b83; margin: 0 auto; }
    table { width: 100%; height: 50px; position: absolute; bottom: 0; background-color: #fff; }
    td.label { text-align: right; padding-right: 10px; font-size: 11px; width: 55px; letter-spacing: 0.08em; }
    td.input { }
    input[type="text"] { width: 98%; height: 20px; }
    textarea { height: 175px; }
    
    #editor { position: absolute; bottom: 45px; top: 5px; right: 0; left: 0; }
    
    .hidden { display: none; }
    
    
    .page_title { text-align: center; font-size: 18px; }
    
    .wide_button_wrap { border: 1px solid #eee; padding: 5px; text-align: center; margin: 15px; margin-right: 5px; }
    .wide_button_wrap div { display: inline-block; border: 1px solid #eee; padding: 5px; margin-left: 15px; margin-right: 15px; width: 50px; }
    .wide_button_wrap div:hover { border: 1px solid #999; cursor: pointer; }
    
    .text_input_wrap { }
    
    .page_data_wrap {  }
    
    @media only screen and (max-width: 750px) { /* - Narrow Layout - */
    
     .edit_info_form_data { border: 5px solid #002b36; }

    
    }
    
</style>
Edit HTML and CSS code
<div class="edit_info_form_wrap">
    <div class="edit_info_form_data">
        <form action="../../save_html" enctype="multipart/form-data" method="post">
        
            <div class="text_input_wrap">
                <textarea name="page_html"></textarea>
                <pre id="editor"></pre>
            </div>
            
            <table>

                <tr>
                    <td class="label">Name</td>
                    <td class="input">[!item_data.page_name!]</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align:right;"><input type="submit" value="Save" /></td>
                </tr>
            </table>
            <input type="hidden" name="data_id" ng-value="item.data_id">
            <input type="hidden" name="data_action" value='Add'>
        </form>
    </div><!-- . publish_blog_form_data - -->
</div><!-- . publish_blog_form_wrap - -->

<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
<script src="../../files/ace.js" type="text/javascript" charset="utf-8"></script>
<script>
var textarea = $('textarea').hide();
var editor = ace.edit("editor");
editor.setTheme("ace/theme/solarized_dark");
editor.getSession().setMode("ace/mode/html");
editor.getSession().setUseWrapMode(true);


editor.getSession().on('change', function(){ 
textarea.val(editor.getSession().getValue());
});
</script>
'''



