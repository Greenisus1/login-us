function Animate (num: number, mySprite: Sprite, list: any[], myImage: Image, text: string) {
    animation.runImageAnimation(
    mySprite,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `],
    num,
    false
    )
}
let Username = game.askForString("Create a username")
let Password = game.askForString("Create a password")
let Repeat_password = game.askForString("Repeat password")
if (Repeat_password == Password) {
    game.splash("Is", Password)
    game.splash("correct")
} else if (false) {
	
} else if (false) {
	
} else {
    game.splash("Error")
}
