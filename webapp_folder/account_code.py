
# -*- coding: latin-1 -*-





new_page_welcome = '''<style>

.page_name { border: 1px solid #bbb; margin-top: 35px; }
.page_name p { line-height: 40px; }
.page_name span { letter-spacing: 0.08em; padding: 25px; background-color: #fff; margin-right: 15px; color: #aaa; }

.account_options { border: 1px solid #bbb; margin-top: 35px; }
.account_options p { line-height: 40px; }
.account_options p:hover { background-color: #EDE7F6; }
.account_options span { letter-spacing: 0.08em; padding: 25px; background-color: #fff; margin-right: 15px; color: #aaa; }

</style>
<div class="welcome_wrap">
<span style="font-size:32px;letter-spacing:0.07em;">Ketchum<span style="color:#2aa198;">.today</span></span></p>
  <p>Welcome To Your New Page</p>
  
  <div class="page_name">
    <p><span>Page Name</span>[!item.page_name!]</p>
  </div>
  <a href="../../edit?[!item.data_id!]">
    <div class="page_name">
      <p><span>Edit</span>Layout</p>
  </div></a>
  <div class="account_options">
    <a href="../../account/settings"><p><span>Go To</span> Account Settings</p></a>
    <a href="../../account/price"><p><span>Go To</span> Pricing Options</p></a>
  </div>

</div><!-- . welcome_wrap - -->
'''





account_page = '''<style>

.page_code { outline: 1px solid #eee; min-height: 300px; padding: 10px; }

.page_title {  }

.pane_data { border: 1px solid #268bd2; margin: 25px; padding: 15px; background-color: #fff; }

.plan_wrap { margin: 10px; padding: 15px; border-top: 1px solid #eee; }
.payment_wrap { margin: 10px; padding: 15px; border-top: 1px solid #eee; }
.learn_wrap { margin: 10px; padding: 15px;  }
.upload_wrap { margin: 10px; padding: 15px; border-top: 1px solid #eee; }
.create_wrap { margin: 10px; padding: 15px; border-top: 1px solid #eee;  }
.template_wrap { margin: 10px; padding: 15px; border-top: 1px solid #eee;  }
.template_option { display: inline-block; border: 1px solid #bbb; width: 100px; height: 100px; margin: 10px; }
.template_option:hover { background-color: #bbb; }


.button_wrap { font-size: 12px; text-align: center; border: 1px solid #888; border-radius: 2px; width: 45px; padding: 5px; float: right; }

</style>

<div class="page_code">

  <div class="page_title">My Account Page</div>

  <tabs>
      <pane title="My Info">

  <div class="pane_data">
    <p>Name of Organiztion</p>
    <p>Contact Address</p>
    <p>Email</p>
    <p>Type</p>
    <div class="plan_wrap">
    <p>Type of Plan</p>
    <table>
          <tr>
            <td class="label">Charge <span style="color:#2aa198;">Yearly</span></td>
            <td class="input">&nbsp;
              <input type="radio" name="payment_rate" value="600-Y"> &nbsp; $600 &nbsp; <span style="color:#2aa198;font-size:14px;">/ Year</span></td>
          </tr>
          <tr>
            <td class="label">Charge <span style="color:#2aa198;">Monthly</span></td>
            <td class="input">&nbsp;
              <input type="radio" name="payment_rate" value="50-M"> &nbsp; $50 &nbsp; <span style="color:#2aa198;font-size:14px;">/ Month</span></td>
          </tr>
        </table>
      </div><!-- . plan_wrap - -->
      <div class="payment_wrap">
    <p>Payment Details</p>
    <div class="button_wrap">Open</div>
  </div><!-- . payment_wrap - -->
  </div>
      </pane>
      <pane title="My Page">
        
          <div class="pane_data">
            <div class="learn_wrap">
              <a href="http://learn.elkhorn.io/" target="_blank">
                http://learn.elkhorn.io/</a>
            </div><!-- . learn_wrap - -->
            <div class="upload_wrap">
              <p>Upload HTML File</p>
              <p><input type="file" /></p>
            </div><!-- . upload_wrap - -->
            <div class="create_wrap">
              <p>[<a href=""> link </a>]Create Your Own HTML Code</p>
            </div><!-- . create_wrap - -->
            <div class="template_wrap">
              <p>Select a Page Template [ Options ]</p>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
              <div class="template_option"></div>
            </div><!-- . template_wrap - -->
          </div><!-- . page_data - -->
        </div>
      </pane>
    </tabs>
</div><!-- . page_code - -->
'''


account_settings = '''<style>
.welcome_link { border: 1px solid #bbb; width: 205px; line-height: 45px; font-size: 14px; }
.welcome_link:hover { border: 1px solid #333; }
.welcome_link span { background-color: #fff; color: #777; font-size: 12px; padding: 15px; margin-right: 10px; }


</style>

<div class="account_wrap">

<a href="../../pages/welcome"><div class="welcome_link"><span>Go To</span> Welcome Page</div></a>


  <p>Account Settings</p>

</div><!-- . account_wrap - -->
'''



account_price = '''<style>

.welcome_link { border: 1px solid #bbb; width: 205px; line-height: 45px; font-size: 14px; }
.welcome_link:hover { border: 1px solid #333; }
.welcome_link span { background-color: #fff; color: #777; font-size: 12px; padding: 15px; margin-right: 10px; }


.price_wrap { width: 325px; margin: 0 auto; border: 1px solid #bbb; }
.price_data { position: relative; }
.price_data div:first-child { position: absolute; top: 0; bottom: 0; background-color: #fff; padding: 35px; }
.price_wrap div { display: inline-block; vertical-align: middle; }
.price_wrap div:nth-child(2) { margin-left: 135px; }
</style>

<div class="account_wrap">
<a href="../../pages/welcome"><div class="welcome_link"><span>Go To</span> Welcome Page</div></a>

  <p>Account Price</p>
  
  <div class="price_wrap">
          <div class="price_data">
            <div style="letter-spacing: 0.08em;">Price</div>
            <div>
              <p>$50 <span style="color:#2aa198;font-size:14px;">/ Month</span></p>
              <span style="color:#2aa198;font-size:14px;">or</span>
              <p>$550 <span style="color:#2aa198;font-size:14px;">/ Year</span></p>
            </div>
          </div><!-- . price_data - -->
        </div><!-- . price_wrap - -->

</div><!-- . account_wrap - -->
'''




register_page_login = '''<style>
td.label { text-align: right; padding-right: 10px; font-size: 16px; }
.new_account_wrap {  }
.price_wrap { width: 325px; margin: 0 auto; border: 1px solid #bbb; }
.price_data { position: relative; }
.price_data div:first-child { position: absolute; top: 0; bottom: 0; background-color: #fff; padding: 35px; }
.price_wrap div { display: inline-block; vertical-align: middle; }
.price_wrap div:nth-child(2) { margin-left: 135px; }
@media (min-width: 550px) {
.price_wrap { width: 350px; }

}

</style>
<div class="register_page_wrap">
      
      <div class="new_account_wrap">
          <div style="padding: 5px;">
          <p style="font-size:24px;line-height:48px;">Register A Page On<br />
            <span style="font-size:32px;letter-spacing:0.07em;">Ketchum<span style="color:#2aa198;">.today</span></span></p>
          </div>
        
        <div class="price_wrap">
          <div class="price_data">
            <div style="letter-spacing: 0.08em;">Price</div>
            <div>
              <p>$50 <span style="color:#2aa198;font-size:14px;">/ Month</span></p>
              <span style="color:#2aa198;font-size:14px;">or</span>
              <p>$550 <span style="color:#2aa198;font-size:14px;">/ Year</span></p>
            </div>
          </div><!-- . price_data - -->
        </div><!-- . price_wrap - -->
        
        <div style="text-align: center; margin-top: 35px;">
        <p><img src="../../pics/google_login.png" /></p>
        <p>Sign in with your Google Account<br />
          <span style="font-size:14px;">( <span style="color:#2aa198;">top right of the screen </span>)</span>
        </p></div>
        
      </div><!-- . new_account_wrap -->

  </div><!-- . register_page_wrap - -->
'''

register_page_name = '''<style>

  .new_account_wrap { margin-top: 55px; }
    table { border-collapse: collapse; }
    td.label { color: #aaa; text-align: right; padding-right: 10px; font-size: 14px; }
    tr.page_name { height: 75px; border: 1px solid #bbb; }
    tr.page_name td.label { height: 75px; background-color: #fff; padding: 25px; letter-spacing: 0.08em; }
    tr.page_name td.input { padding: 15px; }
    
    tr.page_logo { height: 75px; }
    tr.social { height: 25px; }
    tr.submit_wrap { height: 75px; }

    td.input input[type="text"] { height: 18px; width: 175px; }
  
  </style>
  <div class="register_page_wrap">
     <p style="font-size:24px;line-height:48px;">Register a page on<br />
      <span style="font-size:32px;letter-spacing:0.07em;">Ketchum<span style="color:#2aa198;">.today</span></span></p>
    <form action="../../register_new_page" method="post">
      <div class="new_account_wrap">
        <table>
          <tr class="page_name">
            <td class="label">Page <span style="color:#2aa198;">Name</span></td>
            <td class="input"><input type="text" name="page_name" /></td>
          </tr>

          <tr class="submit_wrap">
            <td></td>
            <td style="text-align:right;"><input type="submit" value="Register" /></td>
          </tr>
        </table>
      </div><!-- . new_account_wrap -->
    </form>
  </div><!-- . register_page_wrap - -->
'''


register_page_price = '''<style>

  .new_account_wrap { margin-top: 55px; }

    td.label { color: #aaa; text-align: right; padding-right: 10px; font-size: 14px; }
    tr.page_name { height: 75px; }
    tr.page_logo { height: 75px; }
    tr.social { height: 25px; }
    tr.submit_wrap { height: 75px; }

    td.input input[type="text"] { height: 18px; width: 175px; }
  
  </style>
  <div class="register_page_wrap">
     <p style="font-size:24px;line-height:48px;">Register a page on<br />
      <span style="font-size:32px;letter-spacing:0.07em;">Ketchum<span style="color:#2aa198;">.today</span></span></p>
    <form action="../../register_new_page" method="post">
      <div class="new_account_wrap">
        <table>
          <tr>
            <td class="label">Charge <span style="color:#2aa198;">Yearly</span></td>
            <td class="input">&nbsp;
              <input type="radio" name="payment_rate" value="600-Y"> &nbsp; $600 &nbsp; <span style="color:#2aa198;font-size:14px;">/ Year</span></td>
          </tr>
          <tr>
            <td class="label">Charge <span style="color:#2aa198;">Monthly</span></td>
            <td class="input">&nbsp;
              <input type="radio" name="payment_rate" value="50-M"> &nbsp; $50 &nbsp; <span style="color:#2aa198;font-size:14px;">/ Month</span></td>
          </tr>
          <tr class="page_name">
            <td class="label">Page <span style="color:#2aa198;">Name</span></td>
            <td class="input"><input type="text" name="page_name" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">Phone</span></td>
            <td class="input"><input type="text" name="page_phone" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">Email</span></td>
            <td class="input"><input type="text" name="page_email" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">URL Link</span></td>
            <td class="input"><input type="text" name="page_url_link" /></td>
          </tr>
          <tr class="social"><td></td><td></td></tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">Facebook</span></td>
            <td class="input"><input type="text" name="page_facebook" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">YouTube</span></td>
            <td class="input"><input type="text" name="page_youtube" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">Instagram</span></td>
            <td class="input"><input type="text" name="page_instagram" /></td>
          </tr>
          <tr>
            <td class="label">Page <span style="color:#2aa198;">Twitter</span></td>
            <td class="input"><input type="text" name="page_twitter" /></td>
          </tr>
          <tr class="page_logo">
            <td class="label">Page <span style="color:#2aa198;">Logo</span></td>
            <td class="input"><input type="file" name="page_logo" /></td>
          </tr>
          <tr class="submit_wrap">
            <td></td>
            <td style="text-align:right;"><input type="submit" value="Register" /></td>
          </tr>
        </table>
      </div><!-- . new_account_wrap -->
    </form>
  </div><!-- . register_page_wrap - -->
'''


page_payment_html = '''

payment page

'''


page_layout_template_html = '''<style>
    td.label { text-align: right; padding-right: 10px; font-size: 16px; }
    .new_account_wrap { width: 350px; }
    .price_wrap { margin-top: 50px; }
    .page_layout_wrap { border-right: 1px solid #ccc; width: 450px; }
  
  </style>
  <div class="page_layout_wrap">
    <div class="page_layout_data">
        
      <p style="font-size:24px;line-height:48px;">Example Page Layout</p>

      <div class="post_list_wrap">
        <div class="post_list_data">

          <div class="post_item_wrap">
            <div class="post_item_data">


            </div><!-- . post_item_data - -->
          </div><!-- . post_item_wrap - -->

        </div><!-- . post_list_data - -->
      </div><!-- . post_list_wrap - -->

    </div><!-- . page_layout_data -- >
  </div><!-- . page_layout_wrap - -->
'''





payment_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px;text-align:center;}
  form{padding: 15px 45px;}
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  .form_title{background: #0D47A1; padding: 10px; color:#fff;}
  .payment-errors{color:red;}
  .stripe_img{margin: 25px auto;}
  button[type='submit']{border-radius:0; border: none; background: #0D47A1; color:#fff; padding: 5px; font-size: 12px;}
  </style>
  <div class="main_wrap">
  <article class="form_wrap">
    <div class="form_title">
      <h3>[!program_chosen!] Program</h3>
      <h3>Price: $[!price!]/month</h3>
    </div>
    <form action="/charge_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
      <span class="payment-errors" ng-show="program_status=='Active'">You have already enrolled in a program.</span>
    <table>
      <tr>
        <td class="label">Name*</td>
        <td class="input"><input type="text" name="client_name" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Email*</td>
        <td class="input"><input type="text" name="client_email" ng-model="client_email" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Program*</td>
        <td class="input"><input type="text" name="client_program" ng-model="program_chosen" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Price*</td>
        <td class="input"><input type="text" name="amout" ng-model="price" required/></td>
      </tr>     
      <tr>
        <td class="label">Phone</td>
        <td class="input"><input type="text" name="client_phone" /></td>
      </tr>   
      <tr>
        <td class="label">Address</td>
        <td class="input"><input type="text" name="client_address" /></td>
      </tr>   
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
        <tr>
          <td></td>
          <td style="text-align:right"><button type="submit" ng-disabled="program_status=='Active'">Subscribe to Program</button></td>
        </tr>
     </table>
     <img class="stripe_img" style="width:200px;" src='/pics/stripe.png'>
    </form>
  </article><!-- - /form_wrap - -->
  </div><!-- . main_wrap -->
'''
payment_success_page_html = '''
  <div class="main_wrap">
  <h2>Thank you for your payment.</h2>
  <h2>You will recieve an email reciept.</h2>
  </div><!-- .main_wrap -->
'''
cancel_program_success_page_html = '''
  <div class="main_wrap">
  <h2>Your have quit the program.</h2>
  </div><!-- . main_wrap -->
'''




