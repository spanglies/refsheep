+++
title = "Spencer"
description = "Very Gay otter"
[extra]
emoji = "🦦"
colors = [
    # Fur Colors
    "#a46b4e","#913a28",
    "#6e3d27", "#d5a984",
    # Flesh
    "#f79084",
    # Shirt/Accent
    "#B847B1",
    # Eyes
    "#87a8a3", "#9da897"]
require_nsfw_in_url = true
nsfw_refsheet = true # :^)
clothed_refsheet = true
zip_download = true
config="content/otter/config.toml"
+++

{{ nsfwtoggle() }}

{{ nsfwdescription(path="content/otter/nsfw.toml") }}

{% card(title="Intro") %}

Spencer is a river otter! He was born and raised in the PNW. 
These are standard markdown formatting inside each card.

{% end %}
{% card(title="Clothes?") %}

***Spencer is often found in no clothing at all.***

If he is wearing clothes, he strongly prefers them to be brightly colored.
{{ nsfwabout(path="content/otter/nsfw.toml") }}

{% end %}
{% card(title="Sex", nsfw=true) %}  

This info appears as a hidden element unless show NSFW is turned on

{% end %}
<!-- These are gallery links -->
{{ gallery(path="content/otter/config.toml") }}

{{ nsfwgallery(path="content/otter/nsfw.toml") }}
