<template>
  <div class="main">
    <form
      id="payment"
      name="payment"
      method="post"
      action="https://sci.interkassa.com/"
      enctype="utf-8"
    >
      <input type="hidden" name="ik_co_id" value="5dd8276a1ae1bd52048b456a" />
      <input type="hidden" name="ik_pm_no" value="ID_4233" />
      <input type="hidden" name="ik_am" value="100.00" />
      <input type="hidden" name="ik_cur" value="RUB" />
      <input type="hidden" name="ik_desc" value="Event Description" />
      <input type="submit" value="Pay" />
    </form>
  </div>
</template>

<script>
export default {
  name: "Test"
};
</script>

<style scoped></style>
