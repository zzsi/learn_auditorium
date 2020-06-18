from auditorium import Show

show = Show("My Show")


@show.slide
def static_content(ctx):
    """
    ## Static content

    Can be added very simply with:

    * Method _docstrings_
    * Calling `show.markdown`
    """

    ctx.markdown("> Like this")


@show.slide
def interactive(ctx):
    ctx.markdown("Enter your name")
    name = ctx.text_input(default="World")
    ctx.markdown(f"> Hello {name}")

