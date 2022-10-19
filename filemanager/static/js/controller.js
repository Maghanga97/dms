var currentTab = 0;
    document.addEventListener("DOMContentLoaded", function(event) {

    showTab(currentTab);

    });



    function showTab(n) {
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
    }
    else if (x[n].id=='tab2'){
        document.getElementById("prevBtn").style.display = "inline";
        var next = document.getElementById("nextBtn");
        // next.onclick="";

    }
    // else if (n==(x.length -1)) {
    // var next = document.getElementById("nextBtn");
    // next.innerHTML = '<i class="fa fa-angle-double-right"></i>';
    else {
    document.getElementById("nextBtn").innerHTML = '<i class="fa fa-angle-double-right"></i>';
    }
    fixStepIndicator(n)
    }

    function nextPrev(n) {
        nextBtn.style.display ="inline";
        var x = document.getElementsByClassName("tab");
        if (n == 1 && !validateForm()) return false;
        x[currentTab].style.display = "none";

        currentTab = currentTab + n;
        if (currentTab >= x.length) {
            document.getElementById("text-message").style.display = "block";
            document.getElementById("nextprevious").style.display = "none";
            document.getElementById("all-steps").style.display = "none";
            document.getElementById("register").style.display = "none";
            // document.getElementById("submit").style.display = "none";

        }

    showTab(currentTab);
    }

    function validateForm() {
        var x, y, i,z,s, valid = true;
        // var nextb = document.getElementById('nextbtn');
        x = document.getElementsByClassName("tab");
        y = x[currentTab].getElementsByTagName("input");
        z = x[currentTab].getElementsByTagName("textarea");
        s = x[currentTab].getElementsByTagName("select");


        for (i = 0; i < y.length; i++) {
            if (y[i].value == "" && y[i].placeholder != "optional" ) {
                y[i].className += " invalid";
                valid = false;
            }
        }

        for (i = 0; i < z.length; i++) {
            if (z[i].value == "") {
                z[i].className += " invalid";
                valid = false;
            }
        }

        for (i = 0; i < s.length; i++) {
            if (s[i].value == "") {
                s[i].className += " invalid";
                valid = false;
            }
        }

        if (valid) {
            document.getElementsByClassName("step")[currentTab].className += " finish";

        }
        // else if(valid && (x[currentTab].id=='tab2')){
        //     nextb.innerHTML='<i class="fa fa-sign-in"></i>';
        //     nextb.type ='submit';
        // }

        return valid;
    }

    function fixStepIndicator(n) {
        var i, x = document.getElementsByClassName("step");
        for (i = 0; i < x.length; i++) {
            x[i].className = x[i].className.replace(" active", "");
        }
        x[n].className += " active";
    }
    // function fixSubmit(){
    //     var nextb = document.getElementById('nextBtn');
    //     var description = document.getElementById('description');
    //      if(description.value != ''){
    //             nextb.type='submit';
    //             nextb.innerHTML = '<i class="fa fa-sign-in"></i>';
    //         }
    // }

    var nextbtn = document.getElementById("nextBtn");
    var report = document.getElementById("id_incident_type");
    var display = document.getElementById("display");
    var showmore = document.getElementById("showmore");

        function showmoreTab(){
        var nextBtn = document.getElementById('nextBtn');
        nextBtn.style.display ="none";
        showmore.style.display="block";

    }
    report.addEventListener('change', function() {
        // alert('You selected: ', this.value);
        var val = report.value;
        display.innerHTML = "";

        if (val == 35) {
            var lbl2 = document.createElement('h6');
            lbl2.innerHTML = "complaining about";
            var complaint_type = document.createElement('select');
            display.appendChild(lbl2);
            display.appendChild(complaint_type);
            var complaints = ['','Billing','Staff','Water','Sewerage'];
            for (var index = 0; index < complaints.length; index++) {
                var el = complaints[index];
            var complaint_option = document.createElement('option');
                complaint_option.innerHTML= el;
                complaint_option.value= el;
                complaint_type.appendChild(complaint_option);
            }

            showmoreTab();
        // var lbl = document.createElement('h6');
        // var txtbox = document.createElement('textarea');
        // txtbox.name = 'id_description';
        // txtbox.id = 'description';
        // txtbox.onclick = "this.className = ''";
        // // txtbox.value = 'Explain your answer';
        // lbl.innerHTML = 'Tell us more';
        // display.appendChild(lbl);
        // display.appendChild(txtbox);

        //else if choice is Query
        }else if(val == 38){
            var lbl2 = document.createElement('h6');
            lbl2.innerHTML = "Asking about";
            var complaint_type = document.createElement('select');
            // complaint_type.setAttribute(placeholder) = 'Please Specify (Tafadhali Thibitisha)';
            display.appendChild(lbl2);
            display.appendChild(complaint_type);
            var complaints = [
                                {name: null,id:null},
                                {name:'New water connection',id:10},
                                {name:'New sewer connection',id:11},
                                {name:'Water bowser',id:12},
                                {name:'Exhauster services',id:13},
                                {name:'Bill balance',id:14}
                            ];
            for (var index = 0; index < complaints.length; index++) {
                var el = complaints[index];
            var complaint_option = document.createElement('option');
                complaint_option.innerHTML= el.name;
                complaint_option.value= el.id;
                complaint_type.appendChild(complaint_option);
            }

            showmoreTab();
        // var nextb = document.getElementById('nextbtn');
        // var lbl = document.createElement('h6');
        // var txtbox = document.createElement('textarea')

        // txtbox.name = 'id_description';
        // txtbox.id = 'description';
        // txtbox.onclick = "this.onkeypress = 'fixSubmit()'";
        // txtbox.onkeypress="alert('You triggered the onkeypress event.')";

        // lbl.innerHTML = 'Tell us more';
        // display.appendChild(lbl);
        // display.appendChild(txtbox);

        }else if(val != 35){
            showmoreTab();
            // var lbl = document.createElement('h6');
            // var txtbox = document.createElement('textarea')
            // txtbox.name = 'id_description';
            // txtbox.id = 'description';
            // txtbox.onclick = "this.className = ''";
            // // txtbox.value = 'Explain your answer';
            // lbl.innerHTML = 'Tell us more';
            // display.appendChild(lbl);
            // display.appendChild(txtbox);
        }
        });