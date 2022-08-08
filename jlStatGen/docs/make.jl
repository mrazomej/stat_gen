using Documenter
using jlStatGen

makedocs(
    sitename = "jlStatGen",
    format = Documenter.HTML(),
    modules = [jlStatGen]
)

# Documenter can also automatically deploy documentation to gh-pages.
# See "Hosting Documentation" and deploydocs() in the Documenter manual
# for more information.
#=deploydocs(
    repo = "<repository url>"
)=#
