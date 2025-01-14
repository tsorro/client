.. TradingStrategy.ai documentation master file, created by
   sphinx-quickstart on Thu Jul 15 09:33:58 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TradingStrategy.ai documentation
================================

.. raw:: html

   <img class="intro" src="_static/intro.png" alt="Decentralised trading bots">

TradingStrategy.ai is a protocol for :term:`on-chain` quantitative finance and trade automation. You can develop and :term:`backtest` trading strategies based on all trades ever happened on any blockchain. Live `data <https://mightyeagle.capitalgram.com/datasets>`_ is available to one minute accuracy.

The ready strategies, or trading bots, can be deployed as :term:`autonomous agents <autonomous agent>` running on :term:`smart contracts <smart contract>`. Strategies then trade on :term:`decentralised exchanges <decentralised exchange>`. After deployed, anyone can invest in and withdraw from the strategies in real time. As trade rules are automated on-chain, anyone can verify the honest execution of the trading strategy.

TradingStrategy.ai integrates with :term:`Jupyter notebook`, :term:`Pandas`, :term:`Backtrader` and other popular quantitative finance toolkits popular in `Python data science ecosystem <http://python.org/>`_.

Build on
--------

.. raw:: html

   <img class="logo" src="_static/logos/ethereum.png" alt="Ethereum">

   <img class="logo logo-smaller" src="_static/logos/python.png" alt="Python">

   <img class="logo" src="_static/logos/pandas.png" alt="Pandas">

   <img class="logo" src="_static/logos/pyarrow.png" alt="PyArrow">

   <img class="logo" src="_static/logos/colab.png" alt="Google Colab">

   <img class="logo" src="_static/logos/plotly.png" alt="Plotly">

Community
---------

`Github repository <https://github.com/miohtama/capitalgram-onchain-dex-quant-data>`_.

Documentation
-------------

Find the documentation for research notebooks and Python APIs below.

.. toctree::
   :maxdepth: 1
   :caption: User documentation

   investors
   algo-creators
   fee-structures
   risks-and-legal

.. toctree::
   :maxdepth: 1
   :caption: Algorithm vendor documentation

   examples/getting-started
   running
   datasets
   learn
   troubleshooting
   development
   glossary

.. toctree::
   :maxdepth: 1
   :caption: Code examples

   examples/plotting
   examples/interactive-charts
   examples/technical-analysis
   examples/pairs
   examples/liquidity-analysis
   examples/fastquant

.. toctree::
   :maxdepth: 1
   :caption: Strategy examples

   algorithms/entropy-monkey
   algorithms/ape-in

.. toctree::
   :maxdepth: 1
   :caption: Protocol

   protocol/overview
   protocol/comparison
   protocol/deploy

.. toctree::
   :maxdepth: 1
   :caption: API documentation

   api/client
   api/reader
   api/exchange
   api/pair
   api/candle
   api/liquidity
   api/chain
   api/timebucket
   api/caip
   api/types
   api/backtrader
   api/matplotlib
   api/fastquant

