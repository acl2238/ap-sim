# COMS W3132 Individual Project

## Author
Adrian Lee, acl2238@columbia.edu

## Project Title
AP Simulator

## Project Description

A short choice based game simulating what it's like to take Jae Woo Lee's COMS3157, or AP. Fully text based with a UI to make in-game choices. Various endings.

## Installation Instructions

to do

## Initial Proposal

A choice based game with user decisions changing the route of the story/ending. 

Game would be a satirical representation of the average experience of students in Jae Woo Lee’s COMS3157 (AP)

The game should run in a loop or a single instance with a “week” counter, letting the player know how far they are into the game (tentatively there will be 16 weeks)

On each week, the player is given a few choices to make (study, do the homework on their own, cheat on the homework, etc)

Visible and hidden attributes change the ending by forking into different if clauses

Ideally I want to achieve at least some level of GUI (buttons for the choices that take mouse input, images that show on the screen with text, etc)

## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

For milestone two - I'd like to get sample text printed to screen via functions and also have a template/function for buttons that take mouse inputs.

| Date               | Milestone                                                                                              | Deliverables                | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| **March&nbsp;29**  | Submit project description                                                                             | README.md                   | proposal   |
| **April&nbsp;5**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                   | approved   |
| **April&nbsp;12**  | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs | milestone1 |
| **April&nbsp;19**  | Progress on implementation (define your own goals)                                                     | Source code, unit tests     | milestone2 |
| **April&nbsp;26**  | Completely (or partially) finished implementation                                                      | Source code, documentation  | milestone3 |
| **May&nbsp;10**    | Final touches (conclusion, documentation, testing, etc.)                                               | Conclusion (README.md)      | conclusion |

## Requirements, Features and User Stories

For the time being, just Pygame, since all the code will be written in there

## Technical Specification

Game runs through pygame. All requirements are included in requirements.txt. Refer to installation instructions to get started.

## System or Software Architecture Diagram

Does not really apply. Game is a fairly simple PyGame game that runs in an event loop, and a counter is iterated to advance the game. 

## Development Methodology

Game was developed by reading PyGame documentation and working with Jan. Game was fully tested manually by myself. Certain code was borrowed from third parties, all parties are credited in the code. 

## Potential Challenges and Roadblocks

PyGame is kind of jank. Other than that, the game was fairly simple. In the future, I want to add sound and make the game playable on a web browser, which may be difficult to port. 

## Conclusion and Future Work

I had alot of fun making this. Most of the creative work in the game was just writing the dialogue, the coding though tricky was somewhat trivial. 

As I mentioned above in Potential Challenges, in the future I would like to port this game to browsers. Also maybe add more content in the game. However, seeing that this was just a fun passion project, I'm happy with how it turned out. 

