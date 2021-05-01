<template>
  <div class="main-container">
    <form>
      <div class="box-container">
        <h2 class="heading">Sign In</h2>
        <div class="form-fields">
          <input
            id="email"
            name="email"
            type="text"
            placeholder="Email Address"
          />
        </div>
        <div class="form-fields">
          <input
            id="password"
            name="password"
            type="text"
            placeholder="Password"
          />
        </div>
        <div class="form-fields">
          <button class="signIn" name="commit" type="submit">Sign In</button>
        </div>
        <div class="login-choice"><span>or Sign In with</span></div>
        <SocialLogin />
      </div>
    </form>
    <div class="footer">
      <p>Don't have an account? <a href="/signup"> Create one now</a></p>
    </div>
  </div>
</template>

<script>
import SocialLogin from "@/components/SocialLogin";
export default {
  name: "login",
  components: {
    SocialLogin,
  },
};
</script>

<style lang="sass" scoped>
.main-container
  margin-top: 10%

.box-container
  padding: 20px
  margin: 0 auto
  width: 400px
  box-shadow: beige
  border: 1px solid #ccc
  border-radius: 5px
  background: #fff

.heading
  text-align: center
  font-weight: 300
  color: #444
  margin: 0 auto 45px
  font-size: 35px
  line-height: 38px
  text-transform: none
  letter-spacing: 0

.form-fields,
.form-fields button
  width: 100%
  margin: 5px 0
  line-height: 28px
  border-radius: 5px

.form-fields input
  width: 100%
  line-height: 40px
  border-radius: 5px
  border-radius: 5px
  border: 1px solid #f1f1f1
  background: #fff
  padding: 0 5px
  font-size: 14px

.signIn
  padding: 10px 32px
  color: white
  font-size: 16px
  font-weight: 400
  background: #15CD72
  text-align: center
  cursor: pointer
  height: auto
  -webkit-appearance: none

.createaccount
  padding: 15px
  background-color: #0069ff
  border: none
  color: #fff
  font-size: 16px
  font-weight: 400
  height: 48px
  line-height: 48px
  padding: 0 32px
  text-align: center
  border-radius: 5px

.center
  text-align: center

.login-choice span
  color: #5b6987
  display: -ms-grid
  display: grid
  font-size: 16px
  width: 100%
  line-height: 40px
  -webkit-box-align: center
  -ms-flex-align: center
  align-items: center
  text-align: center
  -ms-grid-columns: minmax(20px, 1fr) auto minmax(20px, 1fr)
  grid-template-columns: minmax(20px, 1fr) auto minmax(20px, 1fr)
  grid-gap: 19px

  &:after,

  &:before
    content: ""
    border-top: 1px solid #e5e8ed

.signup-buttons
  margin-top: 15px
  display: -webkit-box
  display: -ms-flexbox
  display: flex
  -webkit-box-pack: justify
  -ms-flex-pack: justify
  justify-content: space-between
  position: relative

.signup-buttons svg
  left: 16px
  position: absolute
  top: 50%
  -webkit-transform: translateY(-50%)
  transform: translateY(-50%)

.footer,
.footer a
  text-align: center
</style>