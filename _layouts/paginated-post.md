---
layout: default
---
{% include header.html %}
<main>
<!-- breadcrumb-area -->
<section class="breadcrumb-area grey-bg" style="background-image:url({{site.cover_image}})">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-xl-8 col-md-6">
                <div class="breadcrumb-title sm-size">
                    <h2>{{page.title}}</h2>
                    <h3 style="color:white">{{page.subtitle}}</h3>
                </div>
            </div>
            <div class="col-xl-4 col-md-6 text-left text-md-right">
                <div class="breadcrumb">
                    <ul>
                        <li><a href="{{site.url}}">Home</a></li>
                        <li><a href="/pages/blog">Articles</a></li>
                        <li class="text-white pl-1"> Article-Details</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- blog-details-area -->
<div class="basic-blog-area gray-bg content-area-margin pb-40">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 blog-post-items">
                <div class="blog-wrapper mb-60">
                    <!-- <div class="blog-thumb"> -->
                    <!--     <img src="{{page.post_image}}" alt="{{page.title}}"/> -->
                    <!-- </div> -->
                    <div class="blog-content">

<div class="internal-nav">
<a href="{{ page.index | relative_url }}"><h2>{{ page.title }}</h2></a>
</div>

<div class="internal-nav">
{% for palette in site.palettes %}
    {% assign page_number = forloop.index  | plus: 0 %}
    <a href="{{ palette.url | relative_url }}">{{ page_number }}</a>&nbsp;
{% endfor %}
</div>

<br>

{{ content }}

<h2>Pages</h2>

<div class="internal-nav">
{% for palette in site.palettes %}
    {% assign page_number = forloop.index  | plus: 0 %}
    <a href="{{ palette.url | relative_url }}">{{ page_number }}</a>&nbsp;
{% endfor %}
</div>

                        <div class="row mt-30">
                            <div class="col-xl-6 col-lg-6 col-md-6">
                                <div class="blog-post-tag">
                                 {{page | tags | capitalize}}
                                </div>
                            </div>
                            <!--TODO: restore sharing-->
                            <!--<div class="col-xl-6 col-lg-6 col-md-6">-->
                               <!--{% include social_share.html %}-->
                            <!--</div>-->
                        </div>
                    </div>
                    <!--TODO: restore comments-->
                    <!--<div class="post-comments mt-50">-->
                        <!--<div class="latest-comments">-->
                           <!--{% include disqus_comments.html %}-->
                        <!--</div>-->
                    <!--</div>-->
                </div>
            </div>
            <div class="col-lg-4 sidebar-blog right-side">
              {% include sidebar.html %}
            </div>
        </div>
    </div>
</div>
</main>

