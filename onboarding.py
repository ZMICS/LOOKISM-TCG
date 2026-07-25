import discord
from database import create_player
def create_onboarding():
    embed = discord.Embed(
        title="WELCOME TO LOOKISM TCG",
        description=(
            "In a world governed by strength, reputation, and relentless ambition, "
            "every encounter is an opportunity to ascend or be forgotten.\n\n"

            "Collect formidable fighters, forge an unrivalled roster, and challenge "
            "those audacious enough to stand in your path. Every victory carves your "
            "name deeper into the hierarchy; every defeat demands your evolution.\n\n"

            "You will enter this world with **250 Tokens** and nothing but the potential "
            "to build an empire worthy of recognition.\n\n"

            "Should you choose to proceed, you will first be required to acknowledge "
            "the **Terms & Conduct** governing this world.\n\n"

            "**The hierarchy awaits. Will you remain insignificant or rise above them all?**"
        )
    )
    view = discord.ui.View()
    begin_button = discord.ui.Button(
        label="Begin Journey",
        style=discord.ButtonStyle.success
    )
    no_button = discord.ui.Button(
        label="Nope",
        style=discord.ButtonStyle.danger
    )
    view.add_item(begin_button)
    view.add_item(no_button)
    async def no_callback(button_interaction: discord.Interaction):
        await button_interaction.response.edit_message(
            content=(
                "Very well. The hierarchy will remain indifferent "
                "to your absence."
            ),
            embed=None,
            view=None
        )
    no_button.callback = no_callback
    async def begin_callback(button_interaction: discord.Interaction):
        terms_embed = discord.Embed(
            title="TERMS & CONDUCT",
            description=(
                "**1. Fair Play**\n"
                "Any exploitation of bugs, vulnerabilities, or unintended mechanics "
                "for personal advantage is strictly prohibited.\n\n"

                "**2. Respect**\n"
                "Maintain basic decorum when interacting with other players. "
                "Harassment, targeted abuse, and deliberate disruption will not be tolerated.\n\n"

                "**3. Account Responsibility**\n"
                "You are responsible for all activity associated with your player account.\n\n"

                "**4. Game Integrity**\n"
                "Attempts to manipulate the economy, duplicate assets, or circumvent "
                "established game systems may result in disciplinary action.\n\n"

                "**5. Changes & Administration**\n"
                "The administration reserves the right to modify game mechanics and "
                "take necessary action to preserve the integrity of the game.\n\n"

                "By selecting **Accept**, you acknowledge these terms and officially "
                "commence your journey."
            )
        )
        terms_view = discord.ui.View()
        accept_button = discord.ui.Button(
            label="Accept",
            style=discord.ButtonStyle.success
        )
        deny_button = discord.ui.Button(
            label="Deny",
            style=discord.ButtonStyle.danger
        )
        terms_view.add_item(accept_button)
        terms_view.add_item(deny_button)
        async def accept_callback(accept_interaction: discord.Interaction):
            create_player(
                accept_interaction.user.id,
                accept_interaction.user.name
            )
            await accept_interaction.response.edit_message(
                content=(
                    "Your name has been inscribed into the hierarchy.\n\n"
                    "You have received **250 Tokens**.\n"
                    "Your journey begins now."
                ),
                embed=None,
                view=None
            )
        accept_button.callback = accept_callback
        async def deny_callback(deny_interaction: discord.Interaction):
            await deny_interaction.response.edit_message(
                content=(
                    "You have rejected the terms.\n\n"
                    "Your journey ends before it begins."
                ),
                embed=None,
                view=None
            )
        deny_button.callback = deny_callback
        await button_interaction.response.edit_message(
            embed=terms_embed,
            view=terms_view
        )
    begin_button.callback = begin_callback
    return embed, view
