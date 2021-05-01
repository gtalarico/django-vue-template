<template>
  <div class="loginsuccess-container">
    <h1 style="font-size: 24px">Introduction</h1>
    <div class="para-container">
      <p class="para">
        Welcome to Active Lytics, a data analytics platform to assist active
        management of financial portfolios. The boom in retail active investing
        has led to a need for better tools to help investors make decisions.
        This website is your guide. The first problem we seek to solve is when
        to sell your stocks.
      </p>
      <p class="para">
        Conventional wisdom is to buy and hold for a long time. This allows you
        to pay lower capital gains taxes. However, suppose a stock you own
        suddenly increases in price. In that case, it may be better to liquidate
        that position and reallocate that capital, especially if you don’t
        expect the security to sustain those high prices in the future. Even
        though you pay a higher short-term capital gains tax, if the price
        increases sufficiently, it may still be worth it. This website will
        harvest data from daily stock price movements then factor in different
        capital gains taxes and investment horizons to notify you when you
        should sell your securities.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "introduction",
};
</script>
<style lang="sass" scoped>
.para-container
    width: 50%
    // align-items: center
    .para
        font-size: 18px
</style>
