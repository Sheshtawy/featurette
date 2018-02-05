function FeatureRequest(data) {
    var self = this;
    self.title = ko.observable(data.title).extend({
        isRequired: true,
    });
    self.description = ko.observable(data.description);
    self.client = ko.observable(data.client);
    self.clientPriority = ko.observable(data.clientPriority);
    self.productArea = ko.observable(data.productArea);
    self.targetDate = ko.observable(data.targetDate);

    self.showModal = function() {
        $('#editFeatureRequest').modal()
    }

};

function Client(data) {
    var self = this;
    self.name = data.name;
    self.id = data.id;
};

function MainViewModel() {
    var self = this;
    self.productAreaEnum = ko.observableArray([
         'Policies',
         'Billing',
         'Claims',
         'Reports',
    ]);

    self.clients = ko.observableArray();

    self.featureRequests = ko.observableArray([
        new FeatureRequest({
            title: 'A new very innovative feature request', 
            description: 'This feature request is going to change the app completely into something awesome!', 
            client:{ id: 1, name: 'Client A' }, 
            clientPriority: 1,
            productArea: 'Policies',
            targetDate: Date().toLocaleString()
        }),
        new FeatureRequest({
            title: 'Another very innovative feature request', 
            description: 'This super awesome feature request is going to change the app completely into something awesome!', 
            client:{ id: 2, name: 'Client B' }, 
            clientPriority: 2,
            productArea: 'Policies',
            targetDate: Date().toLocaleString()
        }),
    ]);

    self.modalData = ko.observable(new FeatureRequest(
        {
            title: 'A new very innovative feature request', 
            description: 'This feature request is going to change the app completely into something awesome!', 
            client:{ id: 1, name: 'Client A' }, 
            clientPriority: 1,
            productArea: 'Policies',
            targetDate: Date().toLocaleString()
        }
    ));

    self.setModalData = function(featureRequest) {
        console.log(featureRequest)
        self.modalData(new FeatureRequest(ko.toJS(featureRequest)));
        console.log(self.modalData);
        featureRequest.showModal();
    };

    self.ToggleAddFeature = function() {
        console.log('toogggllee')
        $("#addFeatureRequest").modal();
    }

    self.addFeatureRequest = function() {
        var dataObject = {};
        var data = $('#addFeatureRquestForm').serializeArray();
        console.log($('#addFeatureRquestForm'))
        data.forEach(function(item) {
            dataObject[item.name] = item.value;
        });
        console.log(dataObject, data)
        $.ajax(
            '/feature_requests/',
            {
                contentType: 'application/json;',
                method: 'POST',
                data: JSON.stringify(dataObject),
                success: function (response) {
                    $('#addFeatureRequest').modal('hide');
                    self.featureRequests.push(new FeatureRequest(ko.toJS(response)));
                },
            }
        );

        $('#addFeatureRequest').modal('hide');
    }

    self.updateFeatureRequest = function() {}
}

// extenders 
// validations

var isRequired = function(target, isRequired) {
    
    var validate = function(value) {
        if(isRequired || (!value || value === undefined || value === '')) {
            value.errors ? value.errors['isRequired'] = 'required' : value.errors = { required: 'required' }
        }
    }

    validate(target);
    target.subscribe(validate);

    return target;
}

ko.extenders.isRequired = isRequired;

ko.applyBindings(new MainViewModel(), document.getElementById('#root'));
