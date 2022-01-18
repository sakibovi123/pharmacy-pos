var options = {
    debug: "info",
    modules: {
      toolbar: "#toolbar",
    },
    placeholder: "Compose an epic...",
    readOnly: true,
    theme: "snow",
  };
  var editor = new Quill("#editor", options);

  jQuery(document).ready(function () {
    jQuery("#myTable").DataTable();
  });