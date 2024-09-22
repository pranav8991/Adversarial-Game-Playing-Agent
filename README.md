
# 🏆 Project: Build an Adversarial Game Playing Agent (Knight's Isolation)

---

### 🎉 Welcome to the Madness 🎉

🎯 **Goal**: You are about to embark on a daring journey where you will build an agent that dominates in a game called **Knights Isolation**. Picture this: two knights, 🏇🏽, going at it like gladiators on a grid. But instead of swords, you're arming your agent with cutting-edge search techniques like **minimax** with **alpha-beta pruning** 🔍🌳. (Also, you'll need a custom heuristic! 😎 No pressure!)

Oh, and did I mention? You’ve only got **150 milliseconds** to make your move. Yeah. Welcome to the **Thunderdome**. 😬 

---

## 💡 Introduction 💡

Knights Isolation is a fancy variation of the classic Isolation game. In this version, your knight moves like a real **chess knight** (that tricky "L" shape 🐴). You can move to any open cell that's two rows and one column, or two columns and one row away from the current position. Each move blocks off cells, shrinking your options like a ticking time bomb. The first player to run out of moves? They lose. 👎 The winner? Well, they're the new board king/queen! 👑 

![viz](https://github.com/user-attachments/assets/35e780bb-9414-4a09-ae67-9cfb4beb6fd7)

Let's get started!

---

## ⚙️ Solver Functionality ⚙️

Here's what you're about to unleash:

| **Criteria**                              | **Submission Requirements**                                                                                                                                 |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Minimax with Alpha-Beta Pruning**       | (AUTOGRADED) Your agent correctly implements minimax search with alpha-beta pruning to determine the best move within the time limit (a casual 150 milliseconds!). 🏃‍♂️💨 |
| **Custom Heuristic**                      | (AUTOGRADED) You create a custom heuristic that isn't just a mashup of examples from the lectures. No cheating! 🤓 (Hint: get creative with board position evaluations!) |
| **Opening Book (optional)**               | (AUTOGRADED) Build an opening book of "best moves" for the first 4 plies of the game. Your agent is now a bookworm. 📚 |
| **Monte Carlo Tree Search (optional)**    | (AUTOGRADED) Add some spicy Monte Carlo magic to your agent. No guarantees you'll become the next AI prodigy, but it's cool! 🧠🎲 |

---

## 🚀 How I Survived the Project

### **Step 1: The Beginning of the End (aka Introduction)**

So, you've read the intro. You know the stakes. Now, it's time to **strap in** 🪖 and get your hands dirty. Whether you're using the Udacity Workspace (👾 **cheater mode**!) or setting up everything locally, you're about to kick off this wild ride. ⚙️

🔧 **Workspace Users**: Everything's pre-configured. You lucky soul. 😎  
🖥️ **Local Environment Warriors**: Fire up that terminal and run these commands:
```bash
$ source activate aind  # Activate the aind environment
$ git clone https://github.com/udacity/artificial-intelligence.git  # Get the project files
$ cd "artificial-intelligence/Projects/3_Game Playing"  # Enter the arena
```
You're now officially ready to rumble! 🎮👊

---

### **Step 2: Setting Up the Environment**

Ah, the satisfying smell of fresh code in the morning. 🌞 Time to open up `game_agent.py` and meet your new best friend: the **CustomPlayer** class.

You'll start by implementing the `get_action()` method. The rules? Simple:
1. **Pick a move** 🕹️.
2. **Don't break anything** (especially my soul, dear code). 😭
3. **Submit that move before time runs out**. 

**Sample Code**:
```python
def get_action(self, state):
    import random  # 'Cause sometimes luck is all you got
    self.queue.put(random.choice(state.actions()))
```
💡 **Tip**: Whatever fancy algorithms you end up using, they have to fit within a 150ms limit. 👀 If not, your knight gets stranded in the middle of the battlefield, crying.

---

### **Step 3: Implementing the Agent**

Now, this is where you’ll bring the heat. 🔥 Implement your agent using **minimax** with **alpha-beta pruning** or throw in something extra, like **iterative deepening**. Either way, you’re doing some serious brain gymnastics.

📜 **Rule 1**: Make sure your agent **doesn’t blow up** midway through the game. Crashing = bad. ❌  
📜 **Rule 2**: Your agent should return **valid moves**. Yes, jumping out of the grid is frowned upon. 😅  
📜 **Rule 3**: Do it all within the time limit. 

---

### **Step 4: Heuristic Implementation**

Oh yeah, here comes the real fun! 🎢 You get to develop a custom heuristic that evaluates game states. And no, you can’t just copy/paste what you saw in the lectures. 😬

What could be in your secret sauce?
- **Liberties**: How many moves can your knight make? 🕺
- **Center Control**: Is your knight hanging out on the sides of the board like a scared toddler? Or are they boldly dominating the middle? 🌍
- **Opponent Moves**: We care about your knight’s survival, but don’t forget to make life miserable for the other knight too. 😈

---

### **Step 5: Experiments & Results**

Time to **prove** that your agent isn't just all bark and no bite! 🐕 You'll want to compare your agent against a baseline. Maybe it's the old-fashioned minimax with alpha-beta pruning 🧙, or maybe it's something you created out of sheer genius. Either way, the experiment awaits. 🔬

```bash
$ python run_search.py
```

💻 **Output**: Watch your agent strut its stuff. If it performs better than the baseline, treat yourself to a pizza 🍕! If not, back to the code cave you go. 🛠️

---

### **Step 6: Graphing My Sanity**

Now, the final boss of this project: **Data Analysis**! 📊 

Did your agent obliterate the baseline? Or did it crash and burn spectacularly? Either way, graph the results, make some tables, and tell the world what went wrong (or right). 🖼️

**Sample Question**:  
Why did your custom heuristic make sense? Was it the speed of the search that made the difference? Or was it because your agent moved like a knight on Red Bull? 🏇💨

---

## **🎓 Project Submission Instructions**

You’ve done it! The code works, the graphs are beautiful, and you’re probably just about ready to fall into a coma from all the adrenaline. 💤

Time to submit! 🎉💼

Make sure you have these files in your zip:
- **`my_custom_player.py`**: Your knight in shining armor (pun intended). 🏇
- **`report.pdf`**: Your glorious experiment results, full of graphs, tables, and praise. 📄
- **`data.pickle`**: Your knight’s secret weapon, full of knowledge about the game (if you created an opening book). 🧠

Run the Udacity submit script and wave goodbye to your project (and sanity).
```bash
$ udacity submit
```

---

## 💥 How to Run This Masterpiece 💥

**Running the code**: Just pop this into your terminal like it's the magic spell you’ve been waiting for:
```bash
$ python run_search.py
```
🔍 **Watch your agent dominate** the board like a chess grandmaster hopped up on caffeine. ♟️☕  
💀 **Watch your agent crash** when it runs out of time or hits the wrong heuristic. 😭 Either way, it's a show!

---

## **Conclusion**

Congratulations! You've successfully survived the **Knight's Isolation Gauntlet**. ⚔️ Your agent might be ready for the AI Hall of Fame—or maybe just a cozy corner of the local chess club. Either way, you’ve come a long way.

##Just remember — even the mightiest programmers start with baby steps (and occasional tantrums). And hey, sometimes those baby steps mean seeking help from fellow coders, dissecting their code, and piecing together solutions. So yes, I’ve had my fair share of peeking into others' projects, learning from their work, and figuring out how things tick. It’s all part of the journey. So, maff kar do muja if I borrowed an idea or two along the way—because, in the end, it’s about growing and improving. 😅

Don't forget to celebrate! 🎊🍾 Your agent is now ready to take on the world (or at least some other knights).

---

## 📜 License

This project is licensed under the "Why Did I Choose This?!" License. You’re free to fork, share, or remix it—just promise to send a virtual high-five if you come up with an even cooler solution! 🙌😄
