

class Trader:
    def __init__(self, ticker):
        lg.info('Trader initialized with ticker %s' % ticker)

    # check if tradable: ask the borker/API if "asset" is tradable
        # IN: asset (string)
        # OUT: True (exists) / False (does not exist)

    # set stoploss: takes a price as an input and sets the stoploss
        # IN: entry price
        # OUT: stop loss

    # set take profit: takes a price as an input and sets the takeprofit
        # IN: entry price
        # OUT: take profit

    #  load historical stock data:
        # IN: ticker, interval, entries limit
        # OUT: array with historical data (OHCL)

    # get open positions
        # IN: ticker
        # OUT: boolean (True = already open, False = not open)

    # submit order: gets our order through the API (retry)
        # IN: order data, order type
        # OUT: boolean (True = order went through, False = order did not)

    # cancel order: cancels our order (retry)
        # IN: order id
        # OUT: boolean (True = order cancelled, False = order not cancelled)

    # check position: check whether the position exists or not
        # IN: ticker
        # OUT: boolean (True = order is there, False = order not there)

    # get general trend: detect interesting trend (UP / DOWN / NO TREND)
            # IN: 30 min candles data (Close data)
            # OUT: UP / DOWN / NO TREND (strings)
            #If no trend defined, go back to POINT ECHO

    # get instant trend: confirm the trend detected by GT analysis
        # IN: 5 min candles data (Close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        # If failed go back to POINT DELTA

    # get rsi: perform RSI analysis
        # IN: 5 min candles data (Close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        # If failed go back to POINT DELTA

    # get stochastic: perform STOCHASTIc analysis
    # IN: 5 min candles data (OHLC), output of the GT analysis (UP / DOWN string)
                # OUT: True (confirmed) / False (not confirmed)
                # If failed go back to POINT DELTA

    # enter position mode: check the conditions in parallel once insdie the position
        # IF check take profit -> If True -> close position
            # IN: current gains (earning $)
            # OUT: True / False

        # ELIF check stop loss. If True -> close position
            # IN: current gains (losing $)
            # OUT: True / False

        # ELIF check stochastic crossing. If True -> close position
            # STEP 1: pull 5 minutes OHLC data
                # IN: asset
                # OUT: OHLC data (5 min candles)

            # STEP 2: see whether the stochastic curves are crossing
                # IN: OHLC data (5 min candles)
                # OUT: True / False


    def run():

        #LOOP until timeout reached (ex. 2h) 
        #POINT ECHO: INITIAL CHECK
        # check the position: ask the broker/API if we have an open position with "asset"
            # IN: asset (string)
            # OUT: True (exists) / False (does not exist)

        # load historical data: demand the API the 30 min candles

        # get general trend 

            # LOOP until timeout reached (ex. 30 mins)
            # POINT 2
            # STEP 1: load historical data: demand the API the 5min candles
                # If failed go back to POINT DELTA

            # STEP 2: get instant trend

            # STEP 3: perform RSI analysis

            # STEP 4: perform STOCHASTIC analysis

        # submit order (limit)
            # if False, abort / go back to POINT ECHO

        # check position
            # if False, abort / go back to POINT ECHO

        # LOOP until timeout reached (ex. ~8h)
        # enter position mode
        
        #GET OUT
        # submit order (market)
            # if False, retry until it works

        # check position
            # if False, abort / go back to SUBMIT ORDER

        # wait 15 mins

        # end
