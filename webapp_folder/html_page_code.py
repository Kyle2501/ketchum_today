
# -*- coding: latin-1 -*-





front_page = '''
<style>
.hi { margin-left: 5px; margin-top: 5px; font-size: 32px; width: 425px; border-bottom: 1px solid #eee; letter-spacing: .08em; color: #2aa198; }
.current_condition_wrap { margin-left: 5px; margin-top: 5px; transition: 2s; }
.cam_wrap { margin-left: 5px; transition: 2s; }
.cam_wrap img { width: 100%; transition: 1.3s; }

.page_html_wrap { padding-top: 5px; }
.page_wrap { padding: 5px; }



@media (min-height: 550px) {
.page_html_wrap { padding-top: 25px; }
.page_wrap { padding: 10px; }
}

@media (min-width: 550px) {
.cam_wrap img { width: 250px; }
}

@media (min-width: 600px) {

.cam_wrap img { width: 275px; }

}

@media (min-width: 650px) {

.cam_wrap img { width: 300px; }

}

@media (min-width: 700px) {

.cam_wrap img { width: 350px; }

}


@media (min-width: 900px) {

.cam_wrap img { width: 375px; }

}


@media (min-width: 950px) {
.cam_wrap img { width: 400px; }

}

@media (min-width: 1000px) {
.hi { margin-left: 45px; }
.current_condition_wrap { margin-left: 45px; margin-top: 25px; }
.cam_wrap { margin-left: 45px; }
.cam_wrap img { width: 450px; }

}

@media (min-width: 1150px) {
.cam_wrap img { width: 575px; }
}


@media (min-width: 1250px) {
.cam_wrap img { width: 675px; }
}

</style>

  <div class="page_wrap">
    
    <div class="cam_wrap">
    
    <p><span style="color:#586e75;font-size:42px;font-family: 'Anonymous Pro';">[!weather_today_temp!]</span><span style="color:#839496;font-size:38px;">°F</span> &nbsp; <span style="font-size:14px;padding-left:35px;color:#aaa;font-family: 'Anonymous Pro';">[!weather_today_text!]</span></p>
    <img src="https://s3-us-west-1.amazonaws.com/sunvalley.com/images/webcams/locam_full.jpg" />
<!--    
  <img src="https://s3-us-west-1.amazonaws.com/sunvalley.com/images/webcams/wclouds_full.jpg" />
    -->
    </div><!-- . cam_wrap - -->
    
    <div class="current_condition_wrap">
    <p><span style="color:#2aa198;font-size:36px;">[!day!]</span>&nbsp; <span style="color:#586e75;font-family: 'Anonymous Pro'">[!time!]</span> &nbsp; - &nbsp; <span style="color:#bbb;">Sunset at <span style="font-family: 'Anonymous Pro'">[!weather_today_sunset!]</span></span></p>
    
    </div><!-- . current_condition_wrap - -->

    <div class="hi"><span style="color:#839496;font-size:54px;">Ketchum</span><span style="font-family: 'Anonymous Pro';">.today</span></div>
    
    <a href="../../pages/register"><div class="register_link"><span>Register</span> <p>A New Page</p></div></a>

  </div><!-- - . page_wrap - -->
'''




page_item = '''<style>


</style>


<div>[!page_item.page_name!]</div>
<div ng-bind-html="page_html"></div>

'''












google_ad = '''
  <div class="ad_wrap" ng-show="modal=='on'">
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle"
        style="display:inline-block;width:100%;height:200px"
        data-ad-client="ca-pub-0387298839743731"
        data-ad-slot="9423212164"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
  </div><!-- - . ad_wrap - -->
'''


publish_ad = '''

  <a href="../../publish/news">
    <div class="publish_side_button_wrap" ng-show="modal=='on'">
      <h2>Publish<br><span style="font-size:18px;">Your Own</span><br>News</h2>
      <span class="cc">&#128228;</span>
    </div>
  </a><!-- - . publish_side_button - -->

'''


register_ad = '''

  <a href="../../pages/register">
    <div class="publish_side_button_wrap" ng-show="modal=='on'">
      <h2>Register<br><span>Your Own</span><br>Page</h2>
      <span class="cc">&#128228;</span>
    </div>
  </a><!-- - . publish_side_button - -->

'''



pages_page = '''<style>

.welcome_link { border: 1px solid #bbb; width: 205px; line-height: 45px; font-size: 14px; }
.welcome_link:hover { border: 1px solid #333; }
.welcome_link span { background-color: #fff; color: #777; font-size: 12px; padding: 15px; margin-right: 10px; }

.page_select_wrap { width: 300px; outline: 1px solid #eee; padding: 5px; margin-top: 45px; padding-bottom: 25px; }
.page_name_wrap { padding-left: 35px; margin-top: 25px; border-bottom: 1px solid #fff; color: #888; padding-bottom: 10px; }
.page_name_wrap:hover { border-bottom: 1px solid #bbb; cursor: pointer; color: #555; }
</style>
<a href="../../pages/welcome"><div class="welcome_link"><span>Go To</span> Welcome Page</div></a>

<a href="../../pages/register"><div class="register_link"><span>Register</span> <p>A New Page</p></div></a>

<h2>Page <span style="color:#93a1a1;">Listing</span></h2>
<div class="page_select_wrap">
  <div ng-repeat="item in page_list"><a href="../../page?[!item.data_id!]">
    <div class="page_name_wrap">
      [!item.page_name!]
    </div><!-- . page_name_wrap - --></a>
  </div><!-- item repeater - -->
</div><!-- . page_select_wrap - -->

'''

new_page_welcome_html = '''

welcome

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


hi = '''
    
    <p style="line-height:24px;"><span style="color:#586e75;"><span style="font-size:32px;">[!weather_today_temp|safe!]°</span>F</span> &nbsp; [!weather_today_text|safe!]<br /><span style="font-size:14px;">[!weather_today_humidity|safe!]% &nbsp; Humidity<br /><span style="color:#bbb;">Visibility of</span> <span style="color:#586e75;">[!weather_today_visibility|safe!] miles</span></span>
    </p>
    {{ date }}
    
'''



news_page = '''
<h2>News <span style="color:#93a1a1;">Listing</span></h2>
<a href="../../publish/news"><div class="register_button">Publish News</div></a>

'''




events_page = '''
<h2>Event <span style="color:#93a1a1;">Listing</span></h2>

<a href="../../publish/event"><div class="register_button">Publish an Event</div></a>

'''



maps_page = '''<style>
    .map_wrap { outline: 1px solid #eee; bottom: 35px; position: absolute; top: 125px; right: 55px; left: 205px; }
</style>
<link rel="stylesheet" href="../../files/leaflet.css" />
<script src="../../files/leaflet.js"></script>


<h2>Maps <span style="color:#2aa198;">Page</span></h2>

<div class="map_wrap">
  <div id="map" style="width: 100%; height: 80%"></div>
  
  <div class="bottom_wrap">
    <p>
    <span style="color:#2aa198;font-size:30px;padding-left:15px;">[!day!]</span>&nbsp; <span style="color:#586e75;font-family: 'Anonymous Pro';">[!time!]</span> &nbsp; - &nbsp; <span style="color:#bbb;">Sunset at <span style="font-family: 'Anonymous Pro'">[!weather_today_sunset!]</span></span>
    <span style="color:#586e75;font-size:28px;font-family: 'Anonymous Pro';padding-left:35px;">[!weather_today_temp!]</span><span style="color:#839496;font-size:28px;">°F</span>
    </p>
      
  </div><!-- . bottom_wrap - -->
</div><!-- . map_wrap - -->

<script>

  var map = L.map('map').setView([43.6811, -114.367], 14);
  
  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
              attribution: 'Map . Elkhorn Labs',
              maxZoom: 18,
              id: 'kyle2501.cif1jg5a10i7zt0m5ej5doijx',
              accessToken: 'pk.eyJ1Ijoia3lsZTI1MDEiLCJhIjoiY2lmMWpnNm4xMGk2bnRpbTUzeW1qdDQ1ZyJ9.OcoYJjLR7rwfO1r0KSM5Dw'
              }).addTo(map);

</script>

'''









# - Publishing Pages


publish_intro = '''<style>
    .publish_intro_wrap { margin-left: 45px; }
    .button { border-left: 4px solid #fff; padding-left: 20px; margin-left: 30px; margin-bottom: 25px; font-size: 20px; }
    .button:hover { border-left: 4px solid #657b83; }
    .button a { color: #586e75; }
    </style>

<div class="publish_intro_wrap">
    <p style="font-size:32px;color:#2aa198;letter-spacing:0.1em;">Publish</p>
    <div class="button"><a href="../../publish/news">News</a></div>
    <div class="button"><a href="../../publish/event">Event</a></div>
</div><!-- . publish_intro_wrap - -->
'''


create_intro_html = '''
<h2>Create Intro Page</h2>

'''

create_ads_html = '''
<h2>Create Ads Page</h2>

'''


publish_event = '''<style>
     .publish_event_wrap { width: 275px; min-height: 250px; display: inline-block; vertical-align: top; }
     .publish_event_wrap:hover .input_header { border-bottom: 1px solid #888; }
     .publish_event_wrap table { width: 250px; margin: 0 auto; }
     td.label { text-align: right; padding-right: 10px; font-size: 14px; }
     tr { height: 32px; }
      .input_header { text-align: center; font-size: 14px; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #ccc; letter-spacing: .08em; }
      td.input input[type="text"] { height: 20px; width: 165px; text-align: center; border: none; border-bottom: 1px solid #bbb; border-right: 1px solid #ddd; }

    .hour_chooser { display: inline-block; vertical-align: top; margin-left: 35px; }
    .minute_chooser { display: inline-block; margin-top: 30px; margin-left: 15px; }
    .min_select { width: 50px; height: 15px; margin-bottom: 10px; background-color: #EDE7F6; font-family: 'Anonymous Pro', sans-serif; padding: 5px; text-align: center; font-size: 14px; }
    .min_select:hover { background-color: #B2DFDB; cursor: pointer; }

    .time_select { display: inline-block; }

    </style>

<div class="publish_event_wrap" ng-controller="timeCtrl">
  <form action="../../add_event" method="post">
    <div class="input_header">Publish Event</div>
    <table>
      <tr>
        <td class="label">Name</td>
        <td class="input"><input type="text" name="event_name"></td>
      </tr><tr>
        <td class="label">Time</td>
        <td class="input"><input type="text" name="event_name" value="[!event_hour!]"></td>
      </tr>
      <tr>
        <td class="label">Date</td>
        <td class="input"><input type="text" name="event_name"></td>
      </tr>
      <tr>
        <td class="label">Location</td>
        <td class="input"><input type="text" name="event_name"></td>
      </tr>
    </table>
  </form>
  [!event_hour!] hi
</div><!-- . publish_event_wrap - -->

<div class="time_select">
  <div class="hour_chooser"></div>

  <div class="minute_chooser">
    <div class="min_select">:00</div>
    <div class="min_select">:15</div>
    <div class="min_select">:30</div>
    <div class="min_select">:45</div>
  </div><!-- . minute_chooser - -->
</div><!-- . time_select - -->




<script src="../../files/d3.v3.min.js"></script>
<script>
elk.controller('timeCtrl', function($scope) {
  $scope.event_hour = 'hi';



}) //

angular.module('d3', [])
  .factory('d3Service', [function(){
    var d3;
    
           bright = '#EDE7F6';
        dark = '#B2DFDB';

        var clock = d3.select(".hour_chooser")
            .append("svg")
              .attr("width", 200)
              .attr("height", 200)
            .append("g")
              .attr("transform", "translate(100,100)");

        var time = clock.append("text")
            .attr("transform", "translate(0,6)")
            .attr("font-family", 'Anonymous Pro, sans-serif')
            .attr("font-size", "18px")
            .attr("fill", "#073642")
            .style("text-anchor", "middle");

        time.text('');

        var darkenAllUpTo = function (index) {
            clock.selectAll("path")
                .data(index)
                .exit()
                .attr("fill", function (d, i) {
                return (i <= index) ? dark : bright;
            });
        };
        
        var totalHours = 12;
        var singleHour = 12 / totalHours;
            
        var timeFor = function (index) {
            return (index + 1) * singleHour;
        };
        
        var splitClock = function (quantity) {
            var hours = [];
            for(var i = 0; i < quantity; i++){
                hours.push(1);
            }
            return hours; 
        };

        var pie = d3.layout.pie($scope).sort(null);
        var arc = d3.svg.arc($scope).innerRadius(40).outerRadius(80);
        var hours = splitClock(totalHours);

        var setTime = function (selectedHour, $scope) {
            $scope.event_hour = 'l';
            console.log('hththth');

        };

        clock.datum(hours, $scope)
            .selectAll("path")
            .data(pie)
            .enter()
            .append("path")
            .attr("fill", bright)
            .attr("stroke", "#fff")
            .attr("stroke-width", 6)
            .attr("d", arc)

            .on("mouseover", function (d, selectedHour, $scope) {

              darkenAllUpTo(selectedHour); // clock hour color
              time.text(timeFor(selectedHour) + ":00"); // middle text

        })

            .on("click", function (d, selectedHour, $scope) {
              $scope.event_hour = '2';
              setTime();

        });

  }]

</script>

'''
