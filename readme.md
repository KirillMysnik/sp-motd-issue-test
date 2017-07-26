### CS:GO MoTD Issue Reproduction Plugin
This is a Source.Python plugin that reproduces the issue described [here](https://github.com/ValveSoftware/csgo-osx-linux/issues/1483)

#### Installation / Usage
- Download the latest Source.Python build for CS:GO [here](http://builds.sourcepython.com/job/Source.Python/lastSuccessfulBuild/)
- Unpack zip contents to `<Steam Library Path>\common\Counter-Strike Global Offensive\csgo`
- Download the latest version of this plugin: [master.zip](https://github.com/KirillMysnik/sp-motd-issue-test/archive/master.zip)
- Unpack zip contents to the same folder
- Add `-insecure` flag to CS:GO launch arguments via Steam (right click on the game entry -> **Properties** -> **Set launch options...**)
- Start the game
- Type in console: `sp plugin load motd_issue_test`
- Load any map
- Type in chat: `!test`
