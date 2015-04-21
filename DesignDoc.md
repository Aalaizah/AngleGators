AngleGators
===========

An alligator who has to open it's mouth to at least a certain angle to eat
different objects

## Educational Goal

* Understand angles in relation to object sizes
* From Common Core Math Standards 

>    To understand concepts of angles and measure angles

* CCSS.MATH.CONTENT.4.MD.C.5.A

>    An angle is measured with reference to a circle with its center at the
>    common endpoint of the rays, by considering the fraction of the circular
>    arc between the points where the two rays intersect the circle. An angle
>    that turns throught 1/360 of a circle is called a "one-degree angle," and
>    can be used to measure angles.

## Gameplay

* Have 2 conveyor belts if it's too big for the alligator to eat you have to
 move it to the one that doesn't lead to it
* Lose "tooth" if you open too far (to prevent people from just always opening
 all the way)
* Alligator can only open it's mouth `x` degrees
* Conveyor moves faster the longer you play
* Losing `x` teeth gives you a game over
* Alligator gets larger after eating `x` number of items making it's mouth
 open wider.

## Menus and Game Flow

1. Simple Start Menu
    * Play
    * How to Play
    * Credits

    ![Start Menu](http://i.imgur.com/IZC33sB.png)
2. Game Screen
    * Pause button, in top right corner
    * Score/Teeth left, in top corner

    ![Game Screen](http://i.imgur.com/oxJVcGf.png)
3. Pause Screen
    * Return to game
    * Restart game
    * Return to main menu
    * Quit game(exits the application)

    ![Pause Screen](http://i.imgur.com/u1ojNeO.png)
4. How to Play Screen
    * One sentence rundown of the game
    * The control scheme
    * Back button in the bottom left corner

    ![How to Play Screen](http://i.imgur.com/FLKWDII.png)
5. Credits
    * Each of the HFOSS people
    * Artist/Website where art was found
    * Back button in bottom left corner

    ![Credits Screen](http://i.imgur.com/goQOWja.png)

## Art Style

* Simple 2D style with bright colors
* Moodboard/inspiration

![](http://i.imgur.com/cbCxos7.png)
![](http://i.imgur.com/0UAAIjX.png)
![](http://i.imgur.com/af71dTN.png)
![](http://i.imgur.com/2zF1C30.png)
![](http://i.imgur.com/QLDnHw4.png)
![](http://i.imgur.com/mGJ7HTo.png)
![](http://i.imgur.com/0s75Ada.png)

## User Interfaces

* Move mouth open by clicking and dragging
* Mouth angle indicator displays exact degree value
* Score/teeth left in top left corner

## Object Design - Sizes

* No animals being eaten
* Fruits and Veggies

| Food            | Minimum Angle Size (0-90) |
|-----------------|---------------------------|
| Nuts            | 10                        |
| Cherry          | 20                        |
| Grape           | 25                        |
| Kumquats        | 50                        |
| Tomato          | 70                        |
| Celery          | 75                        |
| Potato          | 80                        |
| Head of Lettuce | 90                        |
| Cantaloupe      | 110                       |
| Watermelon      | 120                       |
