# Deep-Q-Network

Normal training:
~~~
python main.py --env_name=Breakout-v0 --is_train=True
~~~

Training with Dueling:
~~~
python main.py --env_name=Breakout-v0 --is_train=True --dueling=True
~~~

Training with Double-Q:
~~~
python main.py --env_name=Breakout-v0 --is_train=True --double_q=True
~~~

Training with Dueling and Double-Q:
~~~
python main.py --env_name=Breakout-v0 --is_train=True --dueling=True --double_q=True 
~~~



__Note:__ `agent.py` and `environment.py` are located at `/dqn/`
